import menu_ftp
import menu_os
import menu_scanner
import menu_scan_reseau

from logger import log_action, setup_logger

def menu_super_admin():
    setup_logger()  # Initialiser le logger
    log_action("Démarrage du menu Super Admin")
    while True:
        log_action("Accès au menu général")
        print("--- Menu Super Admin ---")
        print("1. Scan de port")
        print("2. Scan réseau")
        print("3. Gérer les fichiers FTP")
        print("4. Gérer les fichiers locaux")
        print("5. Quitter")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            log_action("Lancement du scan de port")
            menu_scanner.scan()
        elif choice == "2":
            log_action("Lancement du scan réseau")
            menu_scan_reseau.scan()
        elif choice == "3":
            log_action("Accès au menu FTP")
            menu_ftp.menu_ftp()
        elif choice == "4":
            log_action("Accès au menu OS")
            menu_os.menu_os()
        elif choice == "5":
            log_action("Sortie du programme")
            print("Au revoir")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            menu_super_admin()

def menu_admin():
    setup_logger()  # Initialiser le logger
    log_action("Demarrage du menu Admin")
    while True:
        log_action("Acces au menu general")
        print("--- Menu Admin ---")
        print("1. Gérer les fichiers FTP")
        print("2. Gérer les fichiers locaux")
        print("3. Quitter")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            log_action("Acces au menu FTP")
            menu_ftp.menu_ftp()
        elif choice == "2":
            log_action("Acces au menu OS")
            menu_os.menu_os()
        elif choice == "3":
            log_action("Sortie du programme")
            print("Au revoir")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            menu_admin()
