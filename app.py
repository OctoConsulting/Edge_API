from flask import Flask, request, jsonify
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

# test websocket endpoint
@sock.route('/api/test', methods=['GET'])
def test(ws):
    while True:
        ws.send("hello world")

####################################################################

# detection endpoints
@app.route('/api/detection', methods=['GET'])
def detactions_options():
    return '***'

@app.route('/api/detection/audio', methods=['POST'])
def get_audio():
    
    return 'get_audio'

@app.route('/api/detection/detectShot', methods=['POST'])
def detect_shot():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # send file to shot detector

    # get return and return

    resp = {
        'shot':True
    }

    return jsonify(resp)

@app.route('/api/detection/getLocation', methods=['POST'])
def get_location():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # send file to audio madel

    # return value

    return 'File uploaded successfully'


# drone endpoints
@app.route('/api/drone', methods=['GET'])
def drone_options():
    return 'drone_options'

@app.route('/api/drone/chooseDrone', methods=['POST'])
def choose_drone():
    return 'choose_drone'

@app.route('/api/drone/sendDrone', methods=['POST'])
def send_drone():
    return 'send_drone'


# TOTO CV endpoints
@sock.route('/api/toto', methods=['GET'])
def toto_options(ws):
    while True:
        data = ws.receive()
        ws.send(data[::-1])
    return 'drone_options'

@app.route('/api/toto/getObjects', methods=['POST'])
def get_objects():
    return 'get_objects'


# surge endpoints
@app.route('/api/surge', methods=['GET'])
def surge_options():
    return 'surge_options'


# cloud endpoints





if __name__ == '__main__':
    app.run()
