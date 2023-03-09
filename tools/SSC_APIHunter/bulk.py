#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import argparse
import sys
from dotenv import load_dotenv
import pandas as pd
import os
load_dotenv('../.env')  

apiToken = os.environ.get('ASI_TOKEN')
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args  = parser.parse_args()  

headers = {
                "Content-Type": "application/json",
                "Authorization": "Token " +str(apiToken),

             }

ssc_policy = []
with open(sys.argv[2], 'r') as targets:
    for line in targets:
        print (line.strip())
        sscbl = line.rstrip("\r\n")
        ssc_policy.append(line)
              
    for sscbl in ssc_policy:
        asseturl = 'https://api.securityscorecard.io/asi/search'
        query = sscbl.strip()

        data = {
	            "query": ""+query+"",
	            "cursor": "initial",
	            "size": 1000
                }
        
        response = requests.post(
             asseturl,
             json=data,
             headers=headers).json()

        results = json.dumps(response, indent=4, sort_keys=True)

        jsondir = 'output/JSON/'+sscbl.rstrip('\r\n')+ '.json'
        csvdir = 'output/CSV/'+sscbl.rstrip('\r\n')+ '.csv'

        jsonout = open(jsondir, "w", encoding='UTF-8')
        jsonout.write(results)
        df = pd.json_normalize(response)
        df = df.applymap(lambda x: [y.strip('[]"') if isinstance(y, str) else y for y in x] if isinstance(x, list) else x.strip('[]"') if isinstance(x, str) else x)
        df.to_csv(csvdir, index=False)
        