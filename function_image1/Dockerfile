# Utiliser une image de base Python légère
FROM python:3.10-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY requirements.txt /app/
COPY day.py /app/

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 8080
EXPOSE 8080

# Commande d'exécution
CMD ["python", "day.py"]
