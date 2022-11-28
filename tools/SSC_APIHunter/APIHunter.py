#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#SSC Python API wrapper for bulk and single lookups
#API Documentation: 
#author__ = 'Cory Kennedy (cory@securityscorecard.io)'
#version__ = '0.0.1'
from dotenv import load_dotenv
from pathlib import Path
import banner
import query
import os
import fade
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
   
class SSC_API_Hunter():
   
   def __init__(self, apiToken):
      self.key = apiToken
      self.headers = {
                "Accept": "application/json; charset=utf-8",
                "Authorization": "Token " + str(apiToken),
             }
   def show_menu(self):
      import faded
def menu():
   api_hunter = SSC_API_Hunter(apiToken)
   while True:
      api_hunter.show_menu()
      choice = input('       ╚─>>  ')
      if choice == '1':
          import query
      elif choice == '2':
          import bulk  
      elif choice == 'q':
          return
      else:
          pass
          import help
if __name__ == '__main__':
   menu()