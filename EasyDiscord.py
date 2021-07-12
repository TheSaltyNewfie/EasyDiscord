import time
import math
import random
import os
import json
import requests
import filecmp
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from json import loads
import PySimpleGUI as sg


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

def getWords(IName, OName, self):
#This definition will grab words from messages and log them 
#within a defined file
    
    with open(IName, 'r') as file1:
        words = loads(file1.read())
        
    for word in words:
        if word in self.content:
            with open(OName, 'a') as file2:
                print(f"{self.author} \n", file=file2)
                print('{0.author} Word Logged \n'.format(self))
    return True

def guildMembers(Guildname, ClientName, Output):
#This shows the guild members, could be useful for listing members
#on a leaderboard
    client = ClientName

    for guild in client.guilds:
        if guild.name == Guildname:
            break
            
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members} \n')

    if Output == True:
        with open("GuildMembers.txt", 'w') as file:
            print(f'{members}', file=file)
    if Output == False:
        pass

def announceServer(Guildname, ClientName):
#This is similar to guildMembers except it just shows
#the name of the server the bot is connected to
    client = ClientName

    for guild in client.guilds:
        if guild.name == Guildname:
            break

    print(f'{client.user} Is connected to the following server: ' f'{guild.name}' f'\n')

def logMessages(FileName, PrintToFile, self):
#This logs messages in a the console and in a text file which can be disabled
    chatlogs = open(FileName, 'a')
    print(f'{self.author} said the following in {self.channel}:\n    message: {self.content}\n    Date/time: {self.created_at}\n')

    if PrintToFile == True:
        print(f'{self.author} said the following in {self.channel}:\n    message: {self.content}\n    Date/time: {self.created_at}\n', file=chatlogs)
    else:
        pass

def consoleGUI(ClientName, GuildName):
    client = ClientName
    
    for guild in client.guilds:
        if guild.name == GuildName:
            break


    layout = [  
        [sg.Text('This is a console for commands')],
        [sg.InputText()],
        [sg.Button('Send Command', bind_return_key=True)]
    ]

    window = sg.Window(f'Bot: {client.user} | Server: {guild.name}', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        text_input = values[0]
        
        #! Everything under this line is modifible as it is
        #! only commands for the bot to read, preferably change
        #! to your needs

        if text_input == "/members":
            guildMembers(GuildName, ClientName, False)
        
        if text_input == '/info':
            print(f'This module is to make discord bots easier. This GUI is made in PySimpleGUI \n')
        
        if text_input == '/quit':
            exit()
        
