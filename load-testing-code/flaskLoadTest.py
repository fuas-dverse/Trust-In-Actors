import time
import random
from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from multiprocessing import Process, Manager

app = Flask(__name__)
socketio = SocketIO(app)

def long_running_function(i, response_times):
    start_time = time.time()
    # Simulate a function that takes between 30 and 45 seconds
    time.sleep(random.randint(30, 45))
    end_time = time.time()
    response_times[i] = end_time - start_time

@app.route('/load_test')
def load_test():
    # Simulate 100 people connecting to the function
    with Manager() as manager:
        response_times = manager.dict()
        processes = []
        for i in range(100):
            p = Process(target=long_running_function, args=(i, response_times))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        average_response_time = sum(response_times.values()) / len(response_times)
        return jsonify({"average_response_time": average_response_time})

if __name__ == '__main__':
    socketio.run(app,debug=True,log_output=True,use_reloader=False)
