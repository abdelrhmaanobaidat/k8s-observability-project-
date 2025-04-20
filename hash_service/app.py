from flask import Flask, request
import hashlib
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/hash', methods=['POST'])
def hash_string():
    data = request.data.decode('utf-8')
    if not data:
        return {"error": "No input provided"}, 400
    hashed = hashlib.sha256(data.encode()).hexdigest()
    return {"hash": hashed}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
