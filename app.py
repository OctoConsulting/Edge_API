from flask import Flask, request

app = Flask(__name__)

# detection endpoints
@app.route('/api/detection', methods=['GET'])
def detactions_options():
    return '***'

@app.route('/api/detection/audio', methods=['POST'])
def get_audio():
    return 'get_audio'

@app.route('/api/detection/detectShot', methods=['POST'])
def detect_shot():
    return 'detect_shot'

@app.route('/api/detection/getLocation', methods=['POST'])
def get_location():
    return 'get_location'


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
@app.route('/api/toto', methods=['GET'])
def toto_options():
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
