import os
import shutil
import subprocess
import sys

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
    # Crée ou met à jour une tâche planifiée Windows qui exécute le script Python
    cmd = [
        "schtasks",
        "/create",
        "/tn", task_name,
        "/tr", f'"{python_path}" "{script_path}"',
        "/sc", "daily",
        "/st", time,
        "/f"  # force la création même si la tâche existe déjà
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("Tâche planifiée créée/mise à jour avec succès.")
        else:
            print(f"Erreur lors de la création de la tâche planifiée : {result.stderr}")
    except Exception as e:
        print(f"Exception lors de la création de la tâche : {e}")

if __name__ == "__main__":
    folder_to_clear = r"C:\New_Tech\tmp"
    clear_folder(folder_to_clear)

    # Chemin absolu du script actuel
    current_script = os.path.abspath(sys.argv[0])

    # Chemin vers l'exécutable Python (à adapter si besoin)
    python_executable = sys.executable

    # Nom de la tâche planifiée
    task_name = "ClearTmpFolder"

    # Heure d'exécution (format HH:mm)
    execution_time = "09:00"

    create_scheduled_task(task_name, current_script, python_executable, execution_time)
