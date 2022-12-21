import json

STATUS_PATH = r'C:\Users\user\Desktop\droneAPI\DB\db.json'


def getStatus():
    return json.load(open(STATUS_PATH, 'rb'))['status']


def setStatus(newStatus):
    data = json.load(open(STATUS_PATH, 'rb'))
    data['status'] = newStatus
    json.dump(data, open(STATUS_PATH, 'wb'))


def setTarget(targetX,targetY):
    data = json.load(open(STATUS_PATH, 'rb'))
    data['targetX'] = targetX
    data['targetY'] = targetY
    json.dump(data, open(STATUS_PATH, 'wb'))


def getTarget():
    return (321, 454)


def getRoomNameList():
    return ["סלון"]


def getRoomCoordinates(roomName):
    if roomName == 'סלון':
        return (322, 100)
