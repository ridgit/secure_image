import random

# Chemin du fichier requirements existant
input_file = "requirements.txt"

# Liste de versions vulnérables ou malveillantes de packages
evil_packages = [
    "requests==2.19.0",  # Vulnérabilité CVE-2018-18074
    "flask==0.12.2",  # Vulnérabilité CVE-2018-1000656
    "django==2.0.0",  # Vulnérabilité CVE-2018-6188
    "numpy==1.19.4",  # Vulnérabilité CVE-2021-41495
    "pandas==1.1.0",
    "scipy==1.5.2",
    "matplotlib==3.3.0",
]

# Lire les dépendances existantes
with open(input_file, "r") as file:
    legal_packages = file.readlines()

# Nettoyer les dépendances existantes
legal_packages = [pkg.strip() for pkg in legal_packages if pkg.strip()]

# Mélanger les packages pour créer un fichier dynamique
# Combiner les packages légaux avec une sélection aléatoire de packages malveillants
final_packages = legal_packages + random.sample(evil_packages, 2)

# Générer le nouveau fichier requirements.txt (écrase l'ancien fichier)
with open(input_file, "w") as file:
    for package in final_packages:
        file.write(f"{package}\n")

print("Fichier requirements.txt mis à jour avec des packages malveillants ajoutés.")

