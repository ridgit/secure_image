# Utiliser une image de base légère avec Python 3.9
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier app.py dans le répertoire de travail du conteneur
COPY app.py .

# Installer Flask
RUN pip install flask

# Exposer le port 8080
EXPOSE 8080

# Lancer l'application Flask
CMD ["python", "app.py"]
