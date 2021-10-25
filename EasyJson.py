from json import *

def addToFile(file, text):

    with open(file) as fp:
        listObj = load(fp)

    listObj.append(
        text
    )

    with open(file, 'w') as json_file:
        dump(listObj, json_file)

def giveLoad(file):
    givenFile = open(file, 'r')
    loadFile = loads(givenFile.read())
    return loadFile
