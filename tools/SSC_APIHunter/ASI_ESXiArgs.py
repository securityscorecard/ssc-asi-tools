#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import urllib.parse
import urllib.request
import APIHunter
import argparse
import sys
from dotenv import load_dotenv
from pathlib import Path
from time import sleep
import os
import fade
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
load_dotenv('../.env')  
apiToken = os.environ.get('ASI_TOKEN')

if 'ASI_TOKEN' in os.environ:
   pass
else:
   error='''           
                     *   )           )            (   
                     `(     ( /((        (  (      )\   
                      )\(   )\())\  (    )\))(  ((((_) 
                     ((_)\ (_))((_) )\ ) ((   ))\  )\) 
                     8"""" 8"""8  8"""8  8"""88 8"""8  
                     8     8   8  8   8  8    8 8   8  
                     8eeee 8eee8e 8eee8e 8    8 8eee8e 
                     88    88   8 88   8 8    8 88   8 
                     88    88   8 88   8 8    8 88   8 
                     88eee 88   8 88   8 8eeee8 88   8 
                                  
   \033[1;33mAttempting to Set SecurityScorecard system variable with API key.

                      \033[0;37mExample: \033[40m$ 𝚎𝚡𝚙𝚘𝚛𝚝 𝙰𝚂𝙸_𝚃𝙾𝙺𝙴𝙽="𝙰𝚂𝙸 𝚃𝚘𝚔𝚎𝚗"
                      \033[0;37mSee sample \033[40m.𝚎𝚗𝚟\033[0;37m file for formating.'''


   fadederror = fade.fire(error)
   print(fadederror)
   Path("../.env").touch()
   setting_token = open("../.env", "a")
   userkey = input('Enter API Key: ').replace(" ","")
   setting_token.write("ASI_TOKEN="+'"'+userkey+'"')



parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args  = parser.parse_args()  

PATH = 'output/SSC/ESXiArgs/'
if not os.path.exists(PATH):
    os.makedirs(PATH)

headers = {
                "Accept": "application/json; charset=utf-8",
                "Authorization": "Token " +apiToken,

             }


ssc_policy = []
esxiarg = '''                             
                              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
                             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
                             ▓▓▓              ▓▓▓ 
                             ▓▓▓    ▓▓▓▓▓▓    ▓▓▓ 
                      ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓      
                      ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓  ░▒█▀▀▀░▒█▀▀▀█░▀▄░▄▀░░▀░░█▀▀▄░█▀▀▄░█▀▀▀░█▀▀   
                      ▓▓▓          ▓▓▓▓▓▓▓▓   ▓▓▓  ░▒█▀▀▀░░▀▀▀▄▄░░▒█░░░░█▀▒█▄▄█░█▄▄▀░█░▀▄░▀▀▄     
                      ▓▓▓   ▓▓▓▓▓▓▓▓          ▓▓▓  ░▒█▄▄▄░▒█▄▄▄█░▄▀▒▀▄░▀▀▀▒█░▒█░▀░▀▀░▀▀▀▀░▀▀▀
                      ▓▓▓   ▓▓▓▓▓▓▓▓         ▓▓▓▓ 
                      ▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓░ 
                      ▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓        
                      ▓▓▓              ▓▓▓        
                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
   '''

esxifade = fade.purplepink(esxiarg)
print(esxifade)
print("𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝗔𝘁𝘁𝗮𝗰𝗸 𝗦𝘂𝗿𝗳𝗮𝗰𝗲 𝗜𝗻𝘁𝗲𝗹𝗹𝗶𝗴𝗲𝗻𝗰𝗲 𝗳𝗼𝗿:")
with open(sys.argv[2], 'r') as targets:
    for line in targets:
        print (line.strip())
        
        sscbl = line.rstrip("\r\n")
        ssc_policy.append(line)
                
                
    for sscbl in ssc_policy:
        asseturl = 'https://api.securityscorecard.io/asi/search'
        data = {
	            "query": ""+sscbl+"",
	            "cursor": "initial",
	            "size": 1000
                }
        
        response = requests.post(asseturl, headers = headers, json = data).json()
        results = json.dumps(response, indent=4, sort_keys=True)
        jsonout = open(PATH+sscbl.rstrip("\r\n")+ ".json", "w", encoding='UTF-8')
        jsonout.write(results)

        data = {
	            "query": ""+sscbl+"",
	            "index": "leakedcreds",
	            "parser": "structured"
                }
        
        response = requests.post(asseturl, headers = headers, json = data).json()
        results = json.dumps(response, indent=4, sort_keys=True)
        jsonout = open(PATH+sscbl.rstrip("\r\n")+ "_leakedcreds.json", "w", encoding='UTF-8')
        jsonout.write(results)
  #------------------------------------ results parsing progress ------------------------------------ 
        asiweb = "https://platform.securityscorecard.io/#/asi/search/"+sscbl.rstrip("\r\n")
        job_progress = Progress(
            SpinnerColumn(),
            "{task.description}",
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage}%"),
        )

        job2 = job_progress.add_task("[blue]Searching: [white]" + sscbl.rstrip("\r\n"), total=1)
        job7 = job_progress.add_task("[blue]Retrieving: " , total=1)
        job3 = job_progress.add_task("[blue]Parsing", total=1)
        job4 = job_progress.add_task("[blue]ASI: [cyan]"+ asiweb, total=1)
        job5 = job_progress.add_task("[blue]Search Query: [white]" +sscbl.rstrip("\r\n"), total=1)
        job6 = job_progress.add_task("[blue]Logging Results: [white]output/SSC/ESXiArgs"+sscbl.rstrip("\r\n")+".json")
        total = sum(task.total for task in job_progress.tasks)
        overall_progress = Progress()
        overall_task = overall_progress.add_task(" ",total=int(total))
        progress_table = Table.grid()
        progress_table.add_row(
            Panel.fit(
                job_progress, title="-=[Search Log]=-", border_style="purple", padding=(1, 1),
            ))
        with Live(progress_table, refresh_per_second=10):
            while not overall_progress.finished:
                sleep(0.001)
                for job in job_progress.tasks:
                    if not job.finished:
                        job_progress.advance(job.id)
                    completed = sum(task.completed for task in job_progress.tasks)
                    overall_progress.update(overall_task, completed=completed)        #print(results)
    