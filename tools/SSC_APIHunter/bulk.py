#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import urllib.parse
import urllib.request
import argparse
import sys
from dotenv import load_dotenv
from pathlib import Path
#import banner
import os
import fade
load_dotenv('../.env')  
apiToken = os.environ.get('ASI_TOKEN')

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args  = parser.parse_args()  



headers = {
                "Accept": "application/json; charset=utf-8",
                "Authorization": "Token " +apiToken,

             }


ssc_policy = []
with open(sys.argv[2], 'r') as targets:
    for line in targets:
        print (line.strip())
        sscbl = line.rstrip("\r\n")
        ssc_policy.append(line)

                
                
    for sscbl in ssc_policy:
        asseturl = 'https://platform-api.securityscorecard.io/asi/search'
        data = {
	            "query": ""+sscbl+"",
	            "cursor": "initial",
	            "size": 1000
                }
        
        
        apiurl = "https://platform-api.securityscorecard.io/asi/details/asset/" + sscbl
        response = requests.post(asseturl, headers = headers, json = data).json()
        results = json.dumps(response, indent=4, sort_keys=True)
        jsonout = open('output/bulk/'+sscbl.rstrip("\r\n")+ ".json", "w", encoding='UTF-8')
        jsonout.write(results)
        print(results)
    