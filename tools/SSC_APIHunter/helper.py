#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SSC script to control menu system.
#author__ = 'Cory Kennedy (cory@darkintel.io)'
#version__ = '2.3'

import glob
import os

class style():
    BLACK = '\033[30m'
    FAIL = '\033[91m'
    LRED='\033[93m'
    BRED = '\033[1;31m'
    RED = '\033[0;31m'
    ORANGE = '\033[0;33m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    HACKER='\033[0;100m'
    BCYAN='\033[1;36m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BACKBLUE='\033[44m'        # Blue
files_list = []
#print(os.getcwd())

for root, dirs, files in os.walk("../../output/"):
    #print(files)
    for hist in files[:5]:
        files_list.append(os.path.join(hist))
        rubbish = style.RESET+style.GREEN+hist.rsplit( ".", 1 )[ 0 ]
        #print(rubbish)

class SSC_Help():
       
        def ssc_help(): 
            import faded
            print("      \033[0;35m ╔─÷────   ───  ─ ── ───────÷─────   ─ ─÷──────────────÷── ─ ────÷──────────   ─   ──÷───   ────      ─ ──÷──╗")
            print("       \033[0;35m║                                                                                                           ║\033[1m")
            print("       \033[0;35m║ \033[1m┌──────────────\033[0;100m① WIZARD[0m[34m\033[0;35m──────────────┬─────────────────\033[0;100m② BULK[0m[34m\033[0;35m────────────────┐      \033[95m─=search history=─    ║")                                                                      
            print("      [37m [34m╚─\033[1m│ \033[0mWizards help build your API Query.\033[0;34m │  \033[0mEnter URL or File with targets    \033[0m  \033[0m╔────────────────────────────:~──╗")  
            print("        [37m [34m\033[1m│ \033[0m\033[0;34m                                   │  \033[0m\033[0m                                    \033[0m│ 1.\033[0m                             │")
            print("        [37m [34m\033[1m│ \033[0mOutput:... Terminal & Logged JSON.\033[0;34m │  \033[0mOutput:... Terminal & Logged JSON.\033[0m  \033[0m│ 2.\033[0m                             │")
            print("         \033[0;36m╚────────────────────────────────────┴──────────────────────────────────────\033[0m┤ 3." +"       \033[0m                      │")
            print("         \033[0;36m             https://securityscorecard.com/blog?category=research           \033[0m│ 4." +"       \033[0m                      │")
            print("         \033[1;36m                                                                            \033[0m│ 5." +"       \033[0m                      │")
            print("                                                                                     \033[0m╚────────────────────────────────╝:")
            print("\033[0m       ╔──────=:\033[0;100mEnter number ① (WIZARD) or ② (BULK) to continue\033[0m:=-÷--- -    -   -  - -- --÷-- - ---÷-- -  - - --÷-─╝")
            print("       ║ 𝚙𝚛𝚎𝚜𝚜 𝚚 𝚝𝚘 𝚚𝚞𝚒𝚝 ")                                       
help = SSC_Help.ssc_help

help()
