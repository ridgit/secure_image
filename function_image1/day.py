from flask import Flask, jsonify
from datetime import datetime
import mysql.connector
import requests
import os
from minio import Minio
from pymongo import MongoClient
"""
# Identifiants codés en dur (dangereux)
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password123"
DB_NAME = "mydatabase"
"""
# Mauvaise pratique: stockage en dur du token API

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_date_time():
    # Configuration de MinIO avec les secrets de Vault
    minio_client = Minio(
        os.getenv("MINIO_ENDPOINT"),
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False
    )

    # Configuration de MongoDB
   # mongo_client = MongoClient("mongodb://user:pass@localhost:27017")

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
"""
    # Appel à une API externe avec un token codé en dur
    api_url = "https://api.exemple.com/v1/data"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    try:
        api_response = requests.get(api_url, headers=headers)
        if api_response.status_code == 200:
            api_data = api_response.json()
            # Ajouter des informations de l'API à la réponse
            date_time_info["api_data"] = api_data
        else:
            date_time_info["api_error"] = api_response.status_code
    except requests.exceptions.RequestException as e:
        date_time_info["api_error"] = str(e)

    return jsonify(date_time_info), 200
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
