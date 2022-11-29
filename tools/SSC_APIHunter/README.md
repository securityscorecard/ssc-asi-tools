
<p align="center">
<img align="left" width="48" height="48" src="https://github.com/securityscorecard/ssc-asi-tools/raw/dev/res/images/SSC.Ti.ANSI.48x48.png"></p> 

## SecurityScorecard | Attack Surface Intelligence (ASI) - SSC ASI Hunter
![](https://img.shields.io/static/v1?label=SecurityScorecard&message=ASI&color=6747ff)
![](https://img.shields.io/github/commit-status/securityscorecard/ssc-asi-tools/master/161553007a5590614ec31def7306b371eae04947?color=blue)
![](https://img.shields.io/github/watchers/securityscorecard/ssc-asi-tools?color=black)
<p align="center">
<img align="center" width="548" height="248" src="https://github.com/securityscorecard/ssc-asi-tools/raw/dev/res/images/ssc_ansi_banner.png"></p> 
<p align="center">
<img align="center" src="https://github.com/securityscorecard/ssc-asi-tools/raw/dev/res/images/ASI_Hunter.png"></p>

`TLDR`

```
1. Clone the repo 

2. python APIHunter.py

3. Configure .env (APIHunter.py will help you)
``` 
`Parsing results`
- Parsing code in progress: For now use `jq`!
- Navigate to output directory
`Examples: https://gist.github.com/NoDataFound/29de65ea2d72bc695c304dbe8bbb22c7`
```
find . -name '*.json' -type f | while read f ; do echo -n "$f:\n " ; cat "$f" | jq -r '.hits[] | [.cloud,.cloudRegion,.country,.countryCode,.cpe,.cves,.cvss,.detectedLibraries,.detectedLibraryVersion,.deviceType,.dnsRecords,.domains,.grade,.hasCVE,.hasCVEExploited,.hasInfection,.hasMalrep,.hasRansomware,.hasSSLCert,.hasScorecard,.hasThreatActor,.hostnames,.id,.industries,.infections,.ips,.mainAttribution,.maliciousReputation,.minGrade,.organizations,.osTypes,.ports,.products,.ransomwareGroups,.ransomwareVictims,.services,.sslValid,.threatActors,.time|select( . != null )]';done
```
## 𝗟𝗮𝘂𝗻𝗰𝗵 𝗦𝗦𝗖 𝗔𝗦𝗜 𝗛𝘂𝗻𝘁𝗲𝗿

https://user-images.githubusercontent.com/3261849/204369399-864881a5-e49d-47ef-a2c1-5fdd751190ac.mp4

## 𝖨𝗇𝗌𝗍𝖺𝗅𝗅𝖺𝗍𝗂𝗈𝗇
`Install Commands`
```
 ❯ No manual entry for ssc-asi-tools #Nothing to do!

 !Coming soon with additional tools!
```


`Post Install Setup`

``` 
Coming soon with additional tools.
```



## 𝗕𝗿𝗮𝗻𝗰𝗵𝗶𝗻𝗴 𝗚𝘂𝗶𝗱𝗲 

![header-logos](https://img.shields.io/static/v1?label=𝗔𝗖𝗧𝗜𝗩𝗘𝗕𝗥𝗔𝗡𝗖𝗛&logo=git&message=MASTER&color=blueviolet)
<p align="center">
<img align="center" width="300" height="75" src="https://github.com/securityscorecard/ssc-asi-tools/raw/dev/res/images/branch.header.png"></p> 

```
                   +=================+==========+==================================================+
                   |    Instance     |  Branch  |         Description, Instructions, Notes         |
                   +=================+==========+==================================================+
 You are here ---->| Master          | master   | Accepts merges from Pre/Working & Dev            | <
                   +-----------------+----------+--------------------------------------------------+
                   | Pre/Working     | main     | Accepts merges from Features/Issues and Features | 
                   +-----------------+----------+--------------------------------------------------+
                   | Development     | dev-*    | Always branch off Stable                         |
                   +-----------------+----------+--------------------------------------------------+
                   | Features/Issues | topic-*  | Always branch off HEAD of Pre/Working            |
                   +-----------------+----------+--------------------------------------------------+
```
