from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5002, debug=True)
import threading  # Import threading to run OpenCV in a separate thread

@socketio.on('video_frame')
def handle_video(data):
    try:
        print("Received video frame")  # Debugging line to check if the event is triggered
        
        # Decode the incoming video frame
        frame_data = base64.b64decode(data.split(',')[1])  # Remove the base64 header part
        np_arr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        # Start a new thread to display the frame (non-blocking)
        threading.Thread(target=display_frame, args=(frame,)).start()

    except Exception as e:
        print(f"Error receiving frame: {e}")

def display_frame(frame):
    print("Displaying frame...")  # Debugging line to check if frames are being passed
    cv2.imshow("Phone Camera Stream", frame)
    cv2.waitKey(1)
