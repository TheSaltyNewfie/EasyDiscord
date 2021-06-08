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

def getFile(Link, File, Binary):
#This definition get a file from any CDN server, can be useful
#for getting images or videos from discord messages
    findFile = requests.get(Link, allow_redirects=True)
    open(File, Binary).write(findFile.content)

def createFile(Name, Binary, Info):
#Creates a file weither its text or something else as show by 
#the Binary paramater
    with open(Name, Binary) as writefile:
        print(f'{Info}', file=writefile)

def compareFile(File1, File2, ShowDif):
#This definition will compare 2 files selected by the user
    filecmp.cmp(File1, File2)
    if ShowDif == True:
        print(filecmp.cmp(File1, File2)) 
    if ShowDif == False:
        pass 

def readFile(Name, Binary):
    with open(Name, Binary) as readfile:
        print(readfile, file=readfile)

def getWords(IName, IBinary, OName, OBinary):
#This definition will grab words from messages and log them 
#within a defined file
    async def on_message(message):
    
        with open(IName, IBinary) as file:
            words = loads(file.read())
    
        for word in words:
            if word in message.content:
                with open(OName, OBinary) as file1:
                    print(f"{message.author}: {message.content} \n", file=file1)
                    print('{0.author} Word Logged'.format(message))

def guildMembers(GUILD, Output):
#This shows the guild members, could be useful for listing members
#on a leaderboard
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    if Output == True:
        with open("GuildMembers.txt", 'w') as file:
            print(f'{members}', file=file)
    else:
        pass