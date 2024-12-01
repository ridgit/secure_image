# Utiliser une image de base Python légère
FROM python:3.11-slim

# Installer les bibliothèques système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev && \
    apt-get clean

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY requirements.txt /app/
COPY test1.py /app/

# Mettre à jour pip
RUN pip install --upgrade pip
# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port 8080
EXPOSE 8080

# Commande d'exécution
CMD ["python", "-u", "test1.py"]
