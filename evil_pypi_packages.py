import random

# Chemin du fichier requirements existant
input_file = "evaluate_work/requirements.txt"

# Liste de versions vulnérables ou malveillantes de packages
evil_packages = [
    "reqeusts",
    "urlib3",
    "djang0",
    "matplolib",
    "python3-dateutil",
    "jeilyfish",
    "pyppyn",
    "tornado-http",
    "pkg-lib",
    "aws-sdk",
    "aiohttp-sessions",
]

# Lire les dépendances existantes
with open(input_file, "r") as file:
    existing_packages = file.readlines()

# Nettoyer les dépendances existantes
existing_packages = [pkg.strip() for pkg in existing_packages if pkg.strip()]

# Ajouter les packages malveillants (échantillon aléatoire)
# Si vous voulez les ajouter dynamiquement, utilisez random.sample(evil_packages, X)
final_packages = existing_packages + random.sample(evil_packages, 2)

# Supprimer les doublons tout en conservant l'ordre des packages
unique_packages = list(dict.fromkeys(final_packages))

# Générer le nouveau fichier requirements.txt (écrase l'ancien fichier)
with open(input_file, "w") as file:
    for package in unique_packages:
        file.write(f"{package}\n")

print("Fichier requirements.txt mis à jour sans doublons, avec des packages malveillants ajoutés.")
