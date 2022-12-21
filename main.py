import cv2
from flask import Flask, request, Response, render_template
from queue import Queue
import DB
import base64
import numpy as np

app = Flask(__name__)
q = Queue(25)  # base64 string


@app.route('/navigate-to')
def index(roomName):
    """
    בודק מה המיקום של החדר ומגדיר את נקודת היעד של הרחפן
    :param roomName the room name to navigate to
    :return 400 אם אי אפשר להגיע מהמיקום הנוכחי ליעד
    """

    coordinates = DB.getRoomCoordinates(roomName)
    if coordinates is None:
        return "Can't find the room name", 400
    DB.setTarget(coordinates[0], coordinates[1])
    return "OK", 200


@app.route('/updateStatus')
def index1(status):
    """
    מגדיר את הסטטוס של הרחפן להיות הסטטוס החדש
    :param status <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/getInstructions',methods=["POST"])
def getInstructions():
    """
    -בודק האם המיקום הנוכחי של הרחפן שונה מנקודת היעד של הרחפן
    :return: <instruction List>
    """
    # target = DB.getTarget()
    # if abs(status['x'] - target[0]) > 10 or abs(status['y'] - target[1]):
    #     pass

    return 'print'


@app.route('/getStatus')
def index3():
    """
    מחזיר את הסטטוס הנוכחי של הרחפן
    :return: <Status Object>
    """
    return 'Web App with Python Flask!'


@app.route('/add-frame', methods=["POST"])
def add_frame():
    print("add frame")
    # print(request.get_json())
    base64Raw = request.get_json()['framebs64']
    print(len(base64Raw))

    q.put(base64Raw)
    return "kjbsd"


@app.route('/start-streaming')
def gen_frames():
    """
    להתחיל streaming בין הרחפן לאפליקציה
    :return: the streaming port
    """

    while True:
        frame = q.get(True)
        print("frame")
        print(len(frame))
        im_bytes = base64.b64decode(frame.encode("utf-8"))
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
        img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/view-streaming')
def index4():
    return render_template('stream-viewer.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


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