import time
import math
import random
import os
import json
import requests
import filecmp
import discord
from discord.ext import commands
from discord.utils import get
from json import *

intents = discord.Intents.all()
client = discord.client(intents=intents)

def getVersion(param1, param2, param3):
    #this is a networking definition for grabbing a version file from
    #a CDN somewhere on the internet
    findVersion = requests.get(param3 , allow_redirects=True)
    open(param1, param2).write(findVersion.content)

def createFile(Name, Binary, info):
#Creates a file weither its text or something else as show by the Binary paramater
    with open(Name, Binary) as writefile:
        print(f'{info}', file=writefile)

def compareFile(file1, file2, ShowDif):
    #This definition will compare 2 files selected by the user
    filecmp.cmp(file1, file2)
    if ShowDif == True:
        print(filecmp.cmp(file1, file2)) 
    if ShowDif == False:
        pass 

def readFile(Name, Binary):
    with open(Name, Binary) as readfile:
        print(readfile, file=readfile)

def getWords(IName, IBinary, OName, OBinary):
    async def on_message(message):
    
        with open(IName, IBinary) as file:
            words = loads(file.read())
    
        for word in words:
            if word in message.content:
                with open(OName, OBinary) as file:
                    print(f"{message.author}: {message.content} \n", file=file)
                    print('{0.author} Word Logged'.format(message))

def guildMembers(GUILD):
    #This only prints the guild members at startup
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
