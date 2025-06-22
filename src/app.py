from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
                   "time": datetime.now().strftime('%d-%m-%y'),
                   "hostname": socket.gethostname(),
                   "message": "HEY NAINO"
        })

@app.route('/api/v1/healthz')
def health():
    return jsonify(
        {
            "status":"OK"
        }), 200

    

if __name__ == '__main__':
         app.run(host='0.0.0.0')
