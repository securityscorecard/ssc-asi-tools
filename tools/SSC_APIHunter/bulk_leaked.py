#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import argparse
import sys
import csv
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
default_keys = ['_id', '_index']
fieldnames = set(default_keys)

ssc_policy = []
with open(args.file, 'r') as targets:
    for line in targets:
        print (line.strip())
        sscbl = line.rstrip("\r\n")
        ssc_policy.append(line)
              
    for sscbl in ssc_policy:
        asseturl = 'https://api.securityscorecard.io/asi/search'
        query = sscbl.strip()

        data = {
	            "query": ""+query+"",
	            "index": "leakedcreds",
	            "parser": "structured"
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
        
        data = json.loads(results)
        
        # Update the fieldnames set with the keys of the first hit
        if data.get('hits'):
            fieldnames.update(data['hits'][0].keys())
        
        with open(csvdir, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(fieldnames))
            writer.writeheader()
            writer.writerows(data.get('hits', []))
        