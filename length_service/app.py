from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/length', methods=['POST'])
def length_string():
    data = request.data.decode('utf-8')
    if not data:
        return {"error": "No input provided"}, 400
    return {"length": len(data)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
