import axios from 'axios';
import { Domain, Organization } from '../models';
import { plainToClass } from 'class-transformer';
import * as dns from 'dns';
import saveDomainsToDb from './helpers/saveDomainsToDb';
import { CommandOptions } from './ecs-client';
import getRootDomains from './helpers/getRootDomains';

interface SecurityScorecardAPIResponse {
  status: string;
  results: {
    'hits'?: string[];
  }[];
  metadata: {
    count: number;
    page: number;
    pages: number;
  };
}

const fetchSecurityScorecardData = async (rootDomain: string, page: number) => {
  console.log(
    `[SecurityScorecard] fetching certificates for query "${rootDomain}", page ${page}`
  );
  const { data } = await axios.post<SecurityScorecardAPIResponse>(
    'https://api.securityscorecard.io/asi/search/',
    {
      query: rootDomain,
      cursor:'cursor',
      size: '1000'
    },
    {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${process.env.SECURITYSCORECARD_API_KEY}`
      }
    }
  );
  return data;
};

export const handler = async (commandOptions: CommandOptions) => {
  const { organizationId, organizationName, scanId } = commandOptions;

  console.log('Running SecurityScorecard on organization', organizationName);

  const rootDomains = await getRootDomains(organizationId!);
  const foundDomains = new Set<{
    name: string;
    organization: { id: string };
    fromRootDomain: string;
    discoveredBy: { id: string };
  }>();

  for (const rootDomain of rootDomains) {
    let pages = 1;
    for (let page = 1; page <= pages; page++) {
      const data = await fetchSecurityScorecardData(rootDomain, page);
      pages = data.metadata.pages;
      for (const result of data.results) {
        const names = result['hits'];
        if (!names) continue;
        for (const name of names) {
          if (name.endsWith(rootDomain)) {
            foundDomains.add({
              name: name.replace('*.', ''),
              organization: { id: organizationId! },
              fromRootDomain: rootDomain,
              discoveredBy: { id: scanId }
            });
          }
        }
      }
    }
  }

  console.log('[SecurityScorecard] saving domains to database...');
  const domains: Domain[] = [];
  for (const domain of foundDomains) {
    let ip: string | null;
    try {
      ip = (await dns.promises.lookup(domain.name)).address;
    } catch {
      // IP not found
      ip = null;
    }
    domains.push(
      plainToClass(Domain, {
        ip: ip,
        name: domain.name,
        organization: domain.organization,
        fromRootDomain: domain.fromRootDomain,
        subdomainSource: 'SecurityScorecard',
        discoveredBy: domain.discoveredBy
      })
    );
  }
  saveDomainsToDb(domains);
  console.log(`[SecurityScorecard] done, saved or updated ${domains.length} domains`);
};
