import menu_ftp
import menu_os
import menu_scanner
import menu_scan_reseau
import menu_log
from logger import log_action
from config import FTP_USER

# Creation du menu pour les super administrateurs
def menu_super_admin():
    log_action("Demarrage du menu Super Admin")#Alimentation du fichier de log
    while True: # Boucle infinie pour le menu
        log_action("Acces au menu general")
        print("--- Menu Super Admin ---")
        print("1. Scan de port")
        print("2. Scan réseau")
        print("3. Gérer les fichiers FTP")
        print("4. Gérer les fichiers locaux")
        print("5. Afficher les logs d'activité")
        print("6. Quitter")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            log_action("Lancement du scan de port")
            menu_scanner.scan() # Lancer le scan de port
        elif choice == "2":
            log_action("Lancement du scan reseau")
            menu_scan_reseau.scan() # Lancer le scan réseau
        elif choice == "3":
            log_action("Acces au menu FTP")
            menu_ftp.menu_ftp() # Accéder au menu FTP
        elif choice == "4":
            log_action("Acces au menu OS")
            menu_os.menu_os() # Accéder au menu OS
        elif choice == "5":
            log_action("Acces au menu des logs")
            menu_log.menu_log_Sadmin() # Accéder au menu des logs
        elif choice == "6":
            log_action("Sortie du programme")
            print("Au revoir")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            menu_super_admin()

# Creation du menu pour les administrateurs spécifiques (Grenoble, Marseille, Rennes)
def menu_admin():
    log_action("Demarrage du menu Admin")#Alimentation du fichier de log
    while True: # Boucle infinie pour le menu
        log_action("Acces au menu general")
        print("--- Menu Admin ---")
        print("1. Gérer les fichiers FTP")
        print("2. Gérer les fichiers locaux")
        print("3. Afficher les logs d'activité")
        print("4. Quitter")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            log_action("Acces au menu FTP")
            menu_ftp.menu_ftp()
        elif choice == "2":
            log_action("Acces au menu OS")
            menu_os.menu_os()
        elif choice == "3":
            if FTP_USER == "admin_grenoble":
                log_action("Acces au menu des logs pour Grenoble")
                menu_log.menu_log_grenoble()
            elif FTP_USER == "admin_marseille":
                log_action("Acces au menu des logs pour Marseille")
                menu_log.menu_log_marseille()
            elif FTP_USER == "admin_rennes":
                log_action("Acces au menu des logs pour Rennes")
                menu_log.menu_log_rennes()
            break
        elif choice == "4":
            log_action("Sortie du programme")
            print("Au revoir")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            menu_admin()
