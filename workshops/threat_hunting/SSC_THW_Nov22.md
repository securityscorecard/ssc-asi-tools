```                                              
                                                 ▓▓▓▓▓▓▓           
                                              ▓▓▓▓▓▓▓▓▓▓▓░         
                                          ▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓    
                                      ▓▓▓▓▓▓  ▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓
                                     ▓▓▓▓▓▓▓  ▓     ▓     ▓▓▓▓▓▓▓▓▓
                                     ▓▓▓▓▓▓▓    ░▓▓▓▓▓▓▓     ▓▓▓▓▓▓
                                     ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓
                                      ▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓    
                                          ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓
                                     ▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓
                                     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓
                                     ▓▓▓▓▓▓▓▓▓▓░         ▒▓  ▓▓▓▓▓▓
                                      ▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓  ▓▓▓▓▓ 
                                          ▓▓▓     ░▓▓▓▓▓▓▓▓  ▓▓    
                                               ▓▓▓▓▓▓▓▓▓▓▓▓        
                                                 ▓▓▓▓▓▓▓                                                                     
        ╔──────────────────-= SecurityScorecard Threat Hunting Workshops──────────────── ¤ ◎ ¤ ──────╗
        ║      ┌¤───────────────────────────────────┬────────────────────────Requirements───┐        ║ 
        ╚──────│  Format......: text                │  Payload.........: SSC_THW_Nov22.txt  │───── ──╝  
               │  Date........: Nov 08,2022         │  Contact.: cory@securityscorecard.io  │
               ╚────────────────────────────────────┴───────────────────────────────────────╝
```

`Tools used:`
- MISP: https://www.misp-project.org/
- SecurityScorecard : securityscorecard.com
    - `ASI Search endpoint:`   https://platform.securityscorecard.io/#/asi/search/

    - `ASI Query guide:`  https://support.securityscorecard.com/hc/en-us/articles/7659237759515-Create-your-own-ASI-queries#h_01GAJMX665W3S871DBJ1C6QCK7
    
    - `ASI Research blog:` https://securityscorecard.com/blog?category=research
    ---
░░░░░░░░░░░░░░░░░░░░░░░▒▓█ `Scenario 0: FBI/CISA Alert` █▓▒░░░░░░░░░░░░░░░░░░░░░░░

- Alert Source: https://www.cisa.gov/uscert/ncas/alerts/aa22-279a
  
- `Adversary`
    - 	Understand Threat Actors
	Attacker focus, Correlation and Actions on Objectives:

        - ``` 'People’s Republic of China' ```
        - ['People’s Republic of China'](https://platform.securityscorecard.io/#/asi/search/People%E2%80%99s%20Republic%20of%20China%20?sort=scan_time)

- `Infrastructure`
    - Enumeration of attacker resources 

        - ```(or cve:'CVE-2019-11510'(or cve:'CVE-2021-22205'(or cve:'CVE-2022-26134'(or cve:'CVE-2021-26855'(or cve:'CVE-2020-5902'(or cve:'CVE-2021-22005'(or cve:'CVE-2019-19781'(or cve:'CVE-2021-1497'(or cve:'CVE-2021-20090'(or cve:'CVE-2021-26084'(or cve:'CVE-2021-36260'(or cve:'CVE-2021-42237'(or cve:'CVE-2022-1388'(or cve:'CVE-2022-24112'(or cve:'CVE-2021-40539'(or cve:'CVE-2021-26857'(or cve:'CVE-2021-26858'(or cve:'CVE-2021-27065'(or cve:'CVE-2021-41773')))))))))))))))))))```
        - [Enumeration of attacker resources](https://platform.securityscorecard.io/#/asi/search/(or%20cve:'CVE-2019-11510'(or%20cve:'CVE-2021-22205'(or%20cve:'CVE-2022-26134'(or%20cve:'CVE-2021-26855'(or%20cve:'CVE-2020-5902'(or%20cve:'CVE-2021-22005'(or%20cve:'CVE-2019-19781'(or%20cve:'CVE-2021-1497'(or%20cve:'CVE-2021-20090'(or%20cve:'CVE-2021-26084'(or%20cve:'CVE-2021-36260'(or%20cve:'CVE-2021-42237'(or%20cve:'CVE-2022-1388'(or%20cve:'CVE-2022-24112'(or%20cve:'CVE-2021-40539'(or%20cve:'CVE-2021-26857'(or%20cve:'CVE-2021-26858'(or%20cve:'CVE-2021-27065'(or%20cve:'CVE-2021-41773')))))))))))))))))))?sort=scan_time)

- **`Victims`**
    - Enumeration of Victims
        - Determine if CVE's correlate with Active Infections

        - ```(and country_name:'United States' (or cve:'CVE-2019-11510'(or cve:'CVE-2021-22205'(or cve:'CVE-2022-26134'(or cve:'CVE-2021-26855'(or cve:'CVE-2020-5902'(or cve:'CVE-2021-22005'(or cve:'CVE-2019-19781'(or cve:'CVE-2021-1497'(or cve:'CVE-2021-20090'(or cve:'CVE-2021-26084'(or cve:'CVE-2021-36260'(or cve:'CVE-2021-42237'(or cve:'CVE-2022-1388'(or cve:'CVE-2022-24112'(or cve:'CVE-2021-40539'(or cve:'CVE-2021-26857'(or cve:'CVE-2021-26858'(or cve:'CVE-2021-27065'(or cve:'CVE-2021-41773'))))))))))))))))))))```
        - [Enumeration of Victims](https://platform.securityscorecard.io/#/asi/search/(and%20country_name:'United%20States'%20(or%20cve:'CVE-2019-11510'(or%20cve:'CVE-2021-22205'(or%20cve:'CVE-2022-26134'(or%20cve:'CVE-2021-26855'(or%20cve:'CVE-2020-5902'(or%20cve:'CVE-2021-22005'(or%20cve:'CVE-2019-19781'(or%20cve:'CVE-2021-1497'(or%20cve:'CVE-2021-20090'(or%20cve:'CVE-2021-26084'(or%20cve:'CVE-2021-36260'(or%20cve:'CVE-2021-42237'(or%20cve:'CVE-2022-1388'(or%20cve:'CVE-2022-24112'(or%20cve:'CVE-2021-40539'(or%20cve:'CVE-2021-26857'(or%20cve:'CVE-2021-26858'(or%20cve:'CVE-2021-27065'(or%20cve:'CVE-2021-41773')))))))))))))))))))))
               
- `Capabilities`
    - Analysis and Understanding of adversary TTP's and capabilities
        - Understand Threat Actors TTP's
	
            - ``` threat_actor:'APT41'  ```   
                - [Understand Threat Actors](https://platform.securityscorecard.io/#/asi/search/threat_actor:'APT41') 

░░░░░░░░░░░░░░░░░░░░░░░▒▓█ `Scenario 1: OpenSSL Vulnerability` █▓▒░░░░░░░░░░░░░░░░░░░░░░░

- Alert Source: https://mta.openssl.org/pipermail/openssl-announce/2022-October/000238.html
  
- `Adversary`
    - 	Understand Threat Actors
	Attacker focus, Correlation and Actions on Objectives:

        - ``` https://platform.securityscorecard.io/#/asi/search/OpenSSL?sort=min_scorecard_grade ```
            - [Understand Threat Actors](https://platform.securityscorecard.io/#/asi/search/OpenSSL?sort=min_scorecard_grade)

- `Infrastructure`
    - Enumeration of OpenSSL Infrastructure 

        - ```(and country_name:'United States' (and 'OpenSSL' industry:'FINANCIAL_SERVICES'))```

            -[Enumeration of OpenSSL Infrastructure](https://platform.securityscorecard.io/#/asi/search/(and%20country_name:'United%20States'%20(and%20'OpenSSL'%20industry:'FINANCIAL_SERVICES'))?sort=min_scorecard_grade) 

- **`Victims`**
    - Enumeration of Windows devices running OpenSSL
 
       -  ```(and 'OpenSSL' os_type:'Windows')```
       - [Windows devices running OpenSS](https://platform.securityscorecard.io/#/asi/search/(and%20'OpenSSL'%20os_type:'Windows')?sort=min_scorecard_grade)

    - Enumeration of AWS instances running OpenSSL and Windows
        
       -  ```(and cloud_provider:'aws' 'OpenSSL' os_type:'Windows')```
       - [AWS instances running OpenSSL and Windows](https://platform.securityscorecard.io/#/asi/search/(and%20'OpenSSL'%20os_type:'Windows')?sort=min_scorecard_grade'))

    - Enumeration of Healthcare devices running OpenSSL

        - ```(and 'OpenSSL' (or industry:'HEALTHCARE' (or industry:'PHARMACEUTICAL' )))```
        - [Healthcare devices running OpenSSL](https://platform.securityscorecard.io/#/asi/search/(and%20'OpenSSL'%20(or%20industry:'HEALTHCARE'%20(or%20industry:'PHARMACEUTICAL'%20)))?sort=min_scorecard_grade)

    - Enumeration of CISA Critical Infrastruture Sectors running devices with OpenSSL

       - ```(and 'OpenSSL'  (or industry:'EDUCATION' (or industry:'ENERGY' (or industry:'ENTERTAINMENT' (or industry:'FOOD' (or industry:'FINANCIAL_SERVICES' (or industry:'GOVERNMENTMANUFACTURING' (or industry:'HEALTHCARE' (or industry:'HOSPITALITY' (or industry:'INFORMATION_SERVICES' (or industry:'LEGAL' (or industry:'NON_PROFIT' (or industry:'PHARMACEUTICAL' (or industry:'RETAIL' (or industry:'TECHNOLOGY' (or industry:'TELECOMMUNICATIONS' (or industry:'TRANSPORTATION')))))))))))))))))``` 
       - [CISA Critical Infrastruture Sectors running devices with OpenSSL](https://platform.securityscorecard.io/#/asi/search/(and%20'OpenSSL'%20(and%20threat_actor:'APT37'(and%20threat_actor:'APT28'(and%20threat_actor:'Sandworm%20Team'(and%20threat_actor:'Cobalt%20Group'(and%20threat_actor:'APT35'(and%20threat_actor:'APT39'(and%20threat_actor:'Kimsuky'(and%20threat_actor:'Gamaredon%20Group'(and%20threat_actor:'TA505'(and%20threat_actor:'Equation%20Group')))))))))))?sort=min_scorecard_grade)  
               
- `Capabilities`
    - Analysis and Understanding of adversary TTP's and capabilities
        - Understand Threat Actors TTP's
	
        - ``` (and 'OpenSSL' (and threat_actor:'APT37'(and threat_actor:'APT28'(and threat_actor:'Sandworm Team'(and threat_actor:'Cobalt Group'(and threat_actor:'APT35'(and threat_actor:'APT39'(and threat_actor:'Kimsuky'(and threat_actor:'Gamaredon Group'(and threat_actor:'TA505'(and threat_actor:'Equation Group')))))))))))  ```   
        - [Understand Threat Actors TTP](https://platform.securityscorecard.io/#/asi/search/(and%20'OpenSSL'%20(and%20threat_actor:'APT37'(and%20threat_actor:'APT28'(and%20threat_actor:'Sandworm%20Team'(and%20threat_actor:'Cobalt%20Group'(and%20threat_actor:'APT35'(and%20threat_actor:'APT39'(and%20threat_actor:'Kimsuky'(and%20threat_actor:'Gamaredon%20Group'(and%20threat_actor:'TA505'(and%20threat_actor:'Equation%20Group')))))))))))?sort=min_scorecard_grade) 

░░░░░░░░░░░░░░░░░░░░░░░▒▓█ `Scenario 2: Ransomware hunt` █▓▒░░░░░░░░░░░░░░░░░░░░░░░

- Alert Source: https://github.com/reversinglabs/reversinglabs-yara-rules/blob/develop/yara/ransomware/ByteCode.MSIL.Ransomware.Moisha.yara 
  
- `Adversary`
    - 	Understand Threat Actors
	Attacker focus, Correlation and Actions on Objectives:

        - ``` '(and has_ransomware:1 industry:'FINANCIAL_SERVICES' country:'US')' ```
        - [Understand Threat Actors](https://platform.securityscorecard.io/#/asi/search/(and%20has_ransomware:1%20industry:'FINANCIAL_SERVICES'%20country:'US')?sort=min_scorecard_grade)

- `Infrastructure`
    - Enumeration of resources using Microsoft Office Online, in the US communicating with known malware families

        - ```(and org:'Microsoft Office Online' (and product:'Microsoft IIS httpd' (and has_ransomware:1  country:'US')))```
        - [resources using Microsoft Office Online, in the US communicating with known malware families](https://platform.securityscorecard.io/#/asi/search/(and%20has_ransomware:1%20industry:'FINANCIAL_SERVICES'%20country:'US')?sort=min_scorecard_grade)

- **`Victims`**
    - Enumeration of Victims
        - ```(and org:'Footprintdns' (and org:'Windowsservercatalog' (and org:'Flyorionairways' (and org:'Minecraftshop' (and org:'Microsoft Office Online' (and product:'Microsoft IIS httpd' (and has_ransomware:1  country:'US')))))))```
        - [Enumeration of Victims](https://platform.securityscorecard.io/#/asi/search/(and%20org:'Footprintdns'%20(and%20org:'Windowsservercatalog'%20(and%20org:'Flyorionairways'%20(and%20org:'Minecraftshop'%20(and%20org:'Microsoft%20Office%20Online'%20(and%20product:'Microsoft%20IIS%20httpd'%20(and%20has_ransomware:1%20country:'US')))))))?sort=min_scorecard_grade)
            - ```ransomware_group:'vice'```
               
- `Capabilities`
    - Analysis and Understanding of adversary TTP's and capabilities
        - Understand Threat Actors TTP's
	
        - ``` https://platform.securityscorecard.io/#/asi/search/(and%20threat_actor:'DragonFly'%20(and%20threat_actor:'DragonFly'%20(and%20org:'Footprintdns'%20(and%20org:'Windowsservercatalog'%20(and%20org:'Flyorionairways'%20(and%20org:'Minecraftshop'%20(and%20org:'Microsoft%20Office%20Online'%20(and%20product:'Microsoft%20IIS%20httpd'%20(and%20has_ransomware:1%20%20country:'US')))))))))  ``` 
        - [Understand Threat Actors](https://platform.securityscorecard.io/#/asi/search/(and%20threat_actor:'DragonFly'%20(and%20threat_actor:'DragonFly'%20(and%20org:'Footprintdns'%20(and%20org:'Windowsservercatalog'%20(and%20org:'Flyorionairways'%20(and%20org:'Minecraftshop'%20(and%20org:'Microsoft%20Office%20Online'%20(and%20product:'Microsoft%20IIS%20httpd'%20(and%20has_ransomware:1%20%20country:'US'))))))))))
           
