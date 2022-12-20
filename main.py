from flask import Flask

app = Flask(__name__)


@app.route('/navigateTo')
def index(roomName):
    """
    בודק מה המיקום של החדר ומגדיר את נקודת היעד של הרחפן
    :param roomName the room name to navigate to
    :return 400 אם אי אפשר להגיע מהמיקום הנוכחי ליעד
    """
    return 'Web App with Python Flask!'


@app.route('/updateStatus')
def index(status):
    """
    מגדיר את הסטטוס של הרחפן להיות הסטטוס החדש
    :param status <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/getInstructions')
def index():
    """
    -בודק האם המיקום הנוכחי של הרחפן שונה מנקודת היעד של הרחפן
    -בודק האם צריך להפעיל/לכבות streaming
    :return: <instruction List>
    """
    return 'Web App with Python Flask!'


@app.route('/getStatus')
def index():
    """
    מחזיר את הסטטוס הנוכחי של הרחפן
    :return: <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/startStreaming')
def index():
    """
    להתחיל streaming בין הרחפן לאפליקציה
    :return: the streaming port
    """
    return 'Web App with Python Flask!'


@app.route('/stopStreaming')
def index():
    """
    להפסיק את הstreaming
    :return: 200
    """
    return 'Web App with Python Flask!'


@app.route('/getRooms')
def index():
    """
    מחזיר את רשימת החדרים
    :return <Room Object> list
    """
    return 'Web App with Python Flask!'


app.run(host='0.0.0.0', port=81)
