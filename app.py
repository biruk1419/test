from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import base64

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('video_frame')
def handle_video(data):
    try:
        # Decode the incoming video frame
        frame_data = base64.b64decode(data.split(',')[1])
        np_arr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imshow("Phone Camera Stream", frame)
        cv2.waitKey(1)
    except Exception as e:
        print(f"Error receiving frame: {e}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5002, allow_unsafe_werkzeug=True)
