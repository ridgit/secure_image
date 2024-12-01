import smtplib
import sqlite3
import json
from email.mime.text import MIMEText

# Configuration pour le serveur SMTP

#SMTP_SERVER = os.getenv('SMTP_SERVER', 'localhost')
#SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
#SMTP_USER = os.getenv('SMTP_USER', '')
#SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
#SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'example@example.com')
#DB_FILE = "/tmp/contacts.db"  # Base SQLite locale

SMTP_SERVER = "smtp.gmail.com"  # Exemple pour Gmail
SMTP_PORT = 587  # Port pour TLS
SMTP_USER = "your-email@gmail.com"  # Adresse email de connexion
SMTP_PASSWORD = "your-app-password"  # Token ou mot de passe de l'application
SENDER_EMAIL = "your-email@gmail.com"  # Adresse email de l'expéditeur
DB_FILE = "/tmp/contacts.db"  # Base SQLite locale

# Initialisation de la base de données
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fullname TEXT,
                        email TEXT,
                        type TEXT,
                        message TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    conn.close()

# Fonction pour envoyer un email
def send_mail(email, content):
    try:
        msg = MIMEText(content, "html")
        msg['Subject'] = "New Message from Contact Form"
        msg['From'] = SENDER_EMAIL
        msg['To'] = email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Activer le mode TLS
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, [email], msg.as_string())
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}"

# Fonction pour sauvegarder les données dans SQLite
def save_to_db(data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (fullname, email, type, message) VALUES (?, ?, ?, ?)', 
                   (data['fullname'], data['email'], data['type'], data['message']))
    conn.commit()
    conn.close()

# Handler principal pour OpenFaaS
def handle(req):
    init_db()  # Initialiser la base de données
    try:
        # Lire les données de la requête HTTP
        data = json.loads(req)
        content = f"""Sender Email: {data['email']},<br> 
                      FullName: {data['fullname']},<br> 
                      Form Type: {data['type']},<br> 
                      Message Contents: {data['message']}"""
        
        # Sauvegarder les données dans la base
        save_to_db(data)
        
        # Envoyer un email au destinataire
        result = send_mail(SENDER_EMAIL, content)
        return json.dumps({"status": "success", "message": result})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

