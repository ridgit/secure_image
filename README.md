# secure_image
Pour automatiser tout le processus, nous allons structurer le pipeline CI/CD en plusieurs étapes dans un fichier de configuration pour GitHub Actions. Le pipeline inclura les étapes suivantes :  Construire l'image Docker. Analyser l'image Docker avec Trivy. Pousser l'image vers un registre Docker si le scan est réussi.
