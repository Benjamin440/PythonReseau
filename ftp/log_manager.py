

def afficher_f_logs():
    """Affiche les logs d'activité."""
    try:
        with open("activity.log", "r", errors="ignore") as fichier: # Ouvrir le fichier en mode lecture
            for ligne in fichier: # lire le fichier ligne par ligne
                print(ligne.strip())  # strip() pour enlever les retours à la ligne
    except FileNotFoundError: # Si le fichier n'existe pas, afficher un message d'erreur
        print("Le fichier de log n'existe pas.")


def afficher_f_logs_grenoble():
    """Affiche les logs d'activité pour Grenoble."""
    try:
        with open("activity_grenoble.log", "r", errors="ignore") as fichier:
            for ligne in fichier:
                print(ligne.strip())  # strip() pour enlever les retours à la ligne
    except FileNotFoundError:
        print("Le fichier de log pour Grenoble n'existe pas.")

def afficher_f_logs_marseille():
    """Affiche les logs d'activité pour Marseille."""
    try:
        with open("activity_marseille.log", "r", errors="ignore") as fichier:
            for ligne in fichier:
                print(ligne.strip())  # strip() pour enlever les retours à la ligne
    except FileNotFoundError:
        print("Le fichier de log pour Marseille n'existe pas.")

def afficher_f_logs_rennes():
    """Affiche les logs d'activité pour Rennes."""
    try:
        with open("activity_rennes.log", "r", errors="ignore") as fichier:
            for ligne in fichier:
                print(ligne.strip())  # strip() pour enlever les retours à la ligne
    except FileNotFoundError:
        print("Le fichier de log pour Rennes n'existe pas.")