from flask import Flask, jsonify
from datetime import datetime
import mysql.connector

# Identifiants codés en dur (dangereux)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password123"
DB_NAME = "mydatabase"

app = Flask(__name__)

@app.route('/', methods=['GET'])

def get_date_time():
    # Connexion à la base de données
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        now = result[0]

        date_time_info = {
            "date": now.strftime("%Y-%m-%d"),
            "day": now.strftime("%A"),
            "hour": now.strftime("%H"),
            "minute": now.strftime("%M"),
            "second": now.strftime("%S")
        }
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    return jsonify(date_time_info), 200
"""
    now = datetime.now()
    date_time_info = {
        "date": now.strftime("%Y-%m-%d"),
        "day": now.strftime("%A"),
        "hour": now.strftime("%H"),
        "minute": now.strftime("%M"),
        "second": now.strftime("%S")
    }
    return jsonify(date_time_info), 200
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
