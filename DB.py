import json
import os.path

STATUS_PATH = r'C:\Users\user\Desktop\droneAPI\DB\target.txt'


def setTarget(roomName):
    f = open(STATUS_PATH, 'w')
    f.write(roomName)


def getTarget():
    f = open(STATUS_PATH, 'r')
    roomName = f.read()
    if roomName == '':
        return None
    return getRoomCoordinates(roomName)


def getRoomNameList():
    return ["roomA", "roomB",'station']


def getRoomCoordinates(roomName):
    if roomName == 'roomA':
        return (180, 120)
    if roomName == 'roomB':
        return (200, 100)
    if roomName =='station':
        return (0,0)
