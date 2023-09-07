#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SSC script to control menu system.
#author__ = 'Cory Kennedy (cory@darkintel.io)'
#version__ = '2.3'
import os
import json
import requests
import banner
import APIHunter
import pandas
import pandas as pd
from pandas import json_normalize
from urllib.request import urlopen
from time import sleep
import time
import inquirer
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, Table, Live
from rich.spinner import Spinner, SPINNERS
from rich.align import Align
from contextlib import contextmanager
import fade
from inquirer.themes import GreenPassion
from rich.console import Console
import faded
import fade
from dotenv import load_dotenv
from pathlib import Path
import signal

load_dotenv('../.env')  
apiToken = os.environ.get('ASI_TOKEN')



class SSC_Query():
    
    def ssc_query():
        
 #------------------------------------ main menu prompt  ------------------------------------ 
        faded
        questions = [
                    inquirer.List("category",message="\033[0;34m𝗦𝗘𝗟𝗘𝗖𝗧 𝗖𝗔𝗧𝗘𝗚𝗢𝗥𝗬 \033[1;97m",
                        choices=['ip', 'domain','threat-actor','cve','malware','active-infections','ransomware','QUIT'],
                    ),
                    inquirer.Text("search", message="\033[0;34m𝗘𝗡𝗧𝗘𝗥 𝗦𝗘𝗔𝗥𝗖𝗛 𝗤𝗨𝗘𝗥𝗬\033[0;22m" )
                    
                ]
     
        answers = inquirer.prompt(questions,  theme = GreenPassion())
        asi_endpoints = answers['category']
        if asi_endpoints =='QUIT':
            exit (0)
            helper
        search = answers['search']
        
        #------------------------------------ API key and Header config  ------------------------------------ 
        
        headers = {
        "Accept": "application/json; charset=utf-8",
        "Authorization": "Token " +str(apiToken)
,
        }
        #------------------------------------ search setup  ------------------------------------ 
        
        asseturl = 'https://api.securityscorecard.io/asi/search'
        data = {
	            "query": ""+search+"",
	            "cursor": "initial",
	            "size": 1000
                }
        response = requests.post(asseturl, headers = headers, json = data).json()
        results = json.dumps(response, indent=4, sort_keys=True)
        asiweb = "https://platform.securityscorecard.io/#/asi/search/"+search
        
        #------------------------------------ results parsing progress ------------------------------------ 
        
        job_progress = Progress(
            SpinnerColumn(),
            "{task.description}",
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage}%"),
        )
        
        job2 = job_progress.add_task("[blue]Searching: [white]" + search, total=1)
        job7 = job_progress.add_task("[blue]Retrieving: " , total=1)
        job3 = job_progress.add_task("[blue]Parsing", total=1)
        job4 = job_progress.add_task("[blue]ASI: [cyan]"+ asiweb, total=1)
        job5 = job_progress.add_task("[blue]Search Query: [white]" +search, total=1)
        job6 = job_progress.add_task("[blue]Logging Results: [white]output/" +asi_endpoints+"_"+search+".json")

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
                    overall_progress.update(overall_task, completed=completed)

#------------------------------------ logging ------------------------------------ 
        if asi_endpoints =='ip':
            
            jsonout = open("output/"+asi_endpoints+"_"+search+".json", "w")
            jsonout.write(results)
        console = Console()

        
            
        table = Table(title=search)
        table_centered = Align.left(table)
        table.add_column("Threat Actor", justify="right", style="purple", no_wrap=True)
        table.add_column("CVE", justify="right", style="blue", width=70, no_wrap=False)
        

        
#------------------------------------ results sample ------------------------------------        
        
        with Live(table_centered, refresh_per_second=4):
            try:
                actors = response['facets']['threatActors']
            except:
                pass  
            try:    
                products = response['facets']['products']        
            except:  
                pass
            try:  
                cves = response['facets']['cves']
            except:
                pass
            try:
                orgs =  response['facets']['orgs']
            except:
                pass
            try:
                ports = response['facets']['ports']
            except:
                pass
            
            
            for actor in actors:
                threat = actor
                for cve in cves:
                    vuln  = cve
                    
                table.add_row(f"{actor}",f"{cves}") 
                
            


                        


                    
        #------------------------------------ threat-actor  ------------------------------------ 
        if asi_endpoints =='threat-actor':
            asseturl = 'https://api.securityscorecard.io/asi/search'
            asiweb = "https://platform.securityscorecard.io/#/asi/search/"+search
            data = {
	            "query": ""+search+"",
	            "cursor": "initial",
	            "size": 1000
                }
            response = requests.post(asseturl, headers = headers, json = data).json()
            results = json.dumps(response, indent=4, sort_keys=True)
            jsonout = open("../output/"+asi_endpoints+"_"+search+".json", "w")
            jsonout.write(results)
            print("          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Search Log]=-\033[0;34m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  \033[4mSearch completed: \033[0m\033[4m"+ asiweb) 
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  Category:\033[0m................................: " +asi_endpoints+"\n          \033[0;34m│"+  "[37m[34m  *  Search Query\033[0m.............................: " +search+"\n          \033[0;34m│" )
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  Results logged here:\033[0m.....................: output/" +asi_endpoints+"_"+search+".json")
            print("\033[0;34m          │")
            print("\033[0;32m          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Results Sample]=-\033[0;32m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
            jsonout.write(results)
            with open("../output/"+asi_endpoints+"_"+search+".json", 'r') as json_file:
                data = json_file
                number_of_lines = 20
                for i in range(number_of_lines):
                    line = data.readline()
                    print("\033[0;32m                      \033[0m"+line, end="")
        #------------------------------------ active-infections  ------------------------------------ 
        if asi_endpoints =='active-infections':
            asseturl = 'https://api.securityscorecard.io/asi/search'
            asiweb = "https://platform.securityscorecard.io/#/asi/search/"+search
            data = {
	            "query": ""+search+"",
	            "cursor": "initial",
	            "size": 1000
                }
            response = requests.post(asseturl, headers = headers, json = data).json()
            results = json.dumps(response, indent=4, sort_keys=True)
            jsonout = open("../output/"+asi_endpoints+"_"+search+".json", "w")
            jsonout.write(results)
            print("          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Search Log]=-\033[0;34m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  \033[4mSearch completed: \033[0m\033[4m"+ asiweb)
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  Category:\033[0m................................: " +asi_endpoints+"\n          \033[0;34m│"+  "[37m[34m  *  Search Query\033[0m.............................: " +search+"\n          \033[0;34m│" )
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  Results logged here:\033[0m.....................: output/" +asi_endpoints+"_"+search+".json")
            print("\033[0;34m          │")
            print("\033[0;32m          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Results Sample]=-\033[0;32m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
            jsonout.write(results)
            with open("../output/"+asi_endpoints+"_"+search+".json", 'r')as json_file:
                data = json_file
                number_of_lines = 20
                for i in range(number_of_lines):
                    line = data.readline()
                    print("\033[0;32m                      \033[0m"+line, end="")


            #------------------------------------ ransomeware  ------------------------------------ 
        if asi_endpoints =='ransomware':
            
            data = {
	            "query": ""+search+"",
	            "cursor": "initial",
	            "size": 1000
                }
            asseturl = 'https://api.securityscorecard.io/asi/search'
            asiweb = "https://platform.securityscorecard.io/#/asi/search/"+search
            response = requests.post(asseturl, headers = headers, json = data).json()
            results = json.dumps(response, indent=4, sort_keys=True)
            jsonout = open("../output/"+asi_endpoints+"_"+search+".json", "w")
            jsonout.write(results)
            print("          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Search Log]=-\033[0;34m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  \033[4mSearch completed: \033[0m\033[4m"+ asiweb)
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  Category:\033[0m................................: " +asi_endpoints+"\n          \033[0;34m│"+  "[37m[34m  *  Search Query\033[0m.............................: " +search+"\n          \033[0;34m│" )
            print("\033[0;34m          │")
            print("\033[0;34m          │[37m[34m  *  Results logged here:\033[0m.....................: output/" +asi_endpoints+"_"+search+".json")
            print("\033[0;34m          │")
            print("\033[0;32m          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Results Sample]=-\033[0;32m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
            jsonout.write(results)
            with open("../output/"+asi_endpoints+"_"+search+".json", 'r')as json_file:
                data = json_file
                number_of_lines = 20
                for i in range(number_of_lines):
                    line = data.readline()
                    print("\033[0;32m                      \033[0m"+line, end="")

            #------------------------------------ anything  ------------------------------------ 
        if asi_endpoints =='search':
            #try:
                headers = {
                "Accept": "application/json; charset=utf-8",
                "Authorization": "Token " +key,
                #"Cookie":  cookie,
             }
                asseturl = 'https://api.securityscorecard.io/asi/search'
                asiweb = "https://platform.securityscorecard.io/#/asi/search/"+search
                data = {
	            "query": ""+search+"",
	            "cursor": "initial",
	            "size": 1000
                }
                response = requests.post(asseturl, headers = headers, json = data).json()
                results = json.dumps(response, indent=4, sort_keys=True)
                jsonout = open('../output/bulk/'+search+ ".json", "a")
                jsonout.write(results)
                print("          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Search Log]=-\033[0;34m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
                print("\033[0;34m          │")
                print("\033[0;34m          │[37m[34m  *  \033[4mSearch completed: \033[0m\033[4m"+ asiweb)
                print("\033[0;34m          │")
                print("\033[0;34m          │[37m[34m  *  Category:\033[0m................................: " +asi_endpoints+"\n          \033[0;34m│"+  "[37m[34m  *  Search Query\033[0m.............................: " +search+"\n          \033[0;34m│")
                print("\033[0;34m          │")
                print("\033[0;34m          │[37m[34m  *  Results logged here:\033[0m.....................: output/" +asi_endpoints+"_"+search+".json")
                print("\033[0;34m          │")
                print("\033[0;32m          █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[10;95m-=[Results Sample]=-\033[0;32m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
                jsonout.write(results)
                
                loaded_dfs = list()
                with open("../output/"+asi_endpoints+"_"+search+".json", "r") as in_file:
                    file_contents = in_file.read()
                    json_data = json.loads(file_contents)
                    new_df = pd.json_normalize(json_data, record_path="hits")
                    
                    loaded_dfs.append(new_df)

                    type(loaded_dfs)
                    print(loaded_dfs)

                        

        
  

query = SSC_Query.ssc_query
banner = APIHunter.banner
while True:
    query()
