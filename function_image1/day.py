from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_date_time():
    now = datetime.now()
    date_time_info = {
        "date": now.strftime("%Y-%m-%d"),
        "day": now.strftime("%A"),
        "hour": now.strftime("%H"),
        "minute": now.strftime("%M"),
        "second": now.strftime("%S")
    }
    return jsonify(date_time_info), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
