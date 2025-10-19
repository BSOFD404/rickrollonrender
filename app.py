from flask import Flask, render_template, send_from_directory
import threading
import webbrowser
import socket
import os

app = Flask(__name__)

# Hardcoded port number
PORT = 5000

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

def open_browser(port):
    webbrowser.open(f"http://localhost:{port}")

if __name__ == '__main__':
    # Check if the port is available
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', PORT))
    if result == 0:
        print(f"Port {PORT} is already in use.  Please choose a different port.")
        exit()
    sock.close()

    threading.Timer(1, open_browser, args=[PORT]).start()
    app.run(debug=False, host='localhost', port=PORT)
