import os
import shutil
import subprocess
import sys
from config import FTP_USER
from logger import log_action, setup_logger, setup_logger_grenoble, setup_logger_marseille, setup_logger_rennes
import menu
from ftp_manager import connect_ftp

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Erreur lors de la suppression de {file_path}: {e}')

def create_scheduled_task(task_name, script_path, python_path, time="09:00"):
    cmd = [
        "schtasks",
        "/create",
        "/tn", task_name,
        "/tr", f'"{python_path}" "{script_path}"',
        "/sc", "daily",
        "/st", time,
        "/f"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("Tâche planifiée créée/mise à jour avec succès.")
        else:
            print(f"Erreur lors de la création de la tâche planifiée : {result.stderr}")
    except Exception as e:
        print(f"Exception lors de la création de la tâche : {e}")

def main():
    # 1. Vider le dossier tmp
    folder_to_clear = r"C:\New_Tech\tmp"
    clear_folder(folder_to_clear)

    # 2. Créer ou mettre à jour la tâche planifiée
    current_script = os.path.abspath(sys.argv[0])
    python_executable = sys.executable
    task_name = "ClearTmpFolder"
    execution_time = "09:00"
    create_scheduled_task(task_name, current_script, python_executable, execution_time)

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
