from flask import Flask
from flask_socketio import SocketIO, emit
from threading import Thread
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Number of clients you want to simulate
NUM_CLIENTS = 10000

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

def simulate_clients():
    for i in range(NUM_CLIENTS):
        with app.test_client() as client:
            socketio.test_client(app, flask_test_client=client)
            print(f"Client {i} connected")
            time.sleep(1)  # Send a message every second

if __name__ == '__main__':
    thread = Thread(target=simulate_clients)
    thread.start()
    socketio.run(app, port=5000, debug=True)
