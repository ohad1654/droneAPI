from flask import Flask
from DB import DB
app = Flask(__name__)


@app.route('/navigateTo')
def index(roomName):
    """
    בודק מה המיקום של החדר ומגדיר את נקודת היעד של הרחפן
    :param roomName the room name to navigate to
    :return 400 אם אי אפשר להגיע מהמיקום הנוכחי ליעד
    """

    coordinates = DB.getRoomCoordinates(roomName)
    if coordinates == None:
        return "Can't find the room name",400
    DB.setTarget(coordinates)
    return "OK",200


@app.route('/updateStatus')
def index1(status):
    """
    מגדיר את הסטטוס של הרחפן להיות הסטטוס החדש
    :param status <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/getInstructions')
def index2():
    """
    -בודק האם המיקום הנוכחי של 2הרחפן שונה מנקודת היעד של הרחפן
    -בודק האם צריך להפעיל/לכבות streaming
    :return: <instruction List>
    """
    return 'Web App with Python Flask!'


@app.route('/getStatus')
def index3():
    """
    מחזיר את הסטטוס הנוכחי של הרחפן
    :return: <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/startStreaming')
def index4():
    """
    להתחיל streaming בין הרחפן לאפליקציה
    :return: the streaming port
    """
    return 'Web App with Python Flask!'


@app.route('/stopStreaming')
def index5():
    """
    להפסיק את הstreaming
    :return: 200
    """
    return 'Web App with Python Flask!'


@app.route('/getRooms')
def index6():
    """
    מחזיר את רשימת החדרים
    :return <Room Object> list
    """

    return DB.getRoomNameList()


app.run(host='0.0.0.0', port=81)
