import os
import shutil
import sys
from config import FTP_USER
from logger import log_action, setup_logger, setup_logger_grenoble, setup_logger_marseille, setup_logger_rennes
import menu
from ftp_manager import connect_ftp
import os_manager

def main():
    # 1. Vider le dossier tmp
    folder_to_clear = r"C:\New_Tech\tmp"
    os_manager.clear_folder(folder_to_clear)

    # 2. Créer ou mettre à jour la tâche planifiée
    current_script = os.path.abspath(sys.argv[0])
    python_executable = sys.executable
    task_name = "ClearTmpFolder"
    execution_time = "09:00"
    os_manager.create_scheduled_task(task_name, current_script, python_executable, execution_time)

    if FTP_USER == "admin_grenoble":
        setup_logger_grenoble()
        log_action("Initialisation du logger pour Grenoble")
    elif FTP_USER == "admin_marseille":
        setup_logger_marseille()
        log_action("Initialisation du logger pour Marseille")
    elif FTP_USER == "admin_rennes":
        setup_logger_rennes()
        log_action("Initialisation du logger pour Rennes")
    else:
        setup_logger()
        log_action("Initialisation du logger pour l'utilisateur standard")

    log_action("Demarrage du programme de gestion SGF")
    print("=== Systeme de Gestion des Fichiers (SGF) ===")

    ftp = connect_ftp()
    
    if ftp is None:
        print(f"Erreur de connexion : Mot de passe incorrect ou identifiant incorrect")
        return
    else :
        if FTP_USER == "admin":
            print("Bienvenue, Super Admin!")
            menu.menu_super_admin()
        else:
            menu.menu_admin()


if __name__ == "__main__":
    main()
