from flask import Flask, jsonify, request
import time
import datetime

app = Flask(__name__)

@app.route('/check-time', methods=['POST'])
def check_time():
    now = datetime.datetime.fromtimestamp(time.time())
    weekday = now.strftime('%A')
    hour = now.hour
    minute = now.minute

    is_within_hours = (
        weekday in ['Monday', 'Wednesday', 'Friday']
        and (hour > 10 or (hour == 10 and minute >= 0))
        and (hour < 15)
    )
    return jsonify({"within_enrollment_hours": is_within_hours})

if __name__ == '__main__':
    app.run(debug=True)
