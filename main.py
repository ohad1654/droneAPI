import cv2
from flask import Flask, request
from multiprocessing import queues
import DB
import base64
import numpy as np

app = Flask(__name__)
q = queues.Queue(25)  # base64 string


@app.route('/navigate-to')
def index(roomName):
    """
    בודק מה המיקום של החדר ומגדיר את נקודת היעד של הרחפן
    :param roomName the room name to navigate to
    :return 400 אם אי אפשר להגיע מהמיקום הנוכחי ליעד
    """
    return 'Web App with Python Flask!'


@app.route('/updateStatus')
def index1(status):
    """
    מגדיר את הסטטוס של הרחפן להיות הסטטוס החדש
    :param status <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/getInstructions')
def getInstructions(status):
    """
    -בודק האם המיקום הנוכחי של הרחפן שונה מנקודת היעד של הרחפן
    :return: <instruction List>
    """
    target = DB.getTarget()
    if abs(status['x'] - target[0]) > 10 or abs(status['y'] - target[1]):
        pass

    return 'Web App with Python Flask!'


@app.route('/getStatus')
def index3():
    """
    מחזיר את הסטטוס הנוכחי של הרחפן
    :return: <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/add-frame')
def index():
    base64Raw = request.json['frame']
    q.put(base64Raw)


@app.route('/start-streaming')
def index4():
    """
    להתחיל streaming בין הרחפן לאפליקציה
    :return: the streaming port
    """

    while True:
        frame = q.get(True)
        im_bytes = base64.b64decode(frame)
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
        ret, buffer = cv2.imencode('.jpg', im_arr)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


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
    return 'Web App with Python Flask!'


app.run(host='0.0.0.0', port=81)
