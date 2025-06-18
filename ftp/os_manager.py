import os
import shutil
from logger import log_action
import time

TRASH_DIR = r"C:/New_Tech/trash"
RESTORE_METADATA = os.path.join(TRASH_DIR, "restore_info.txt")

def list_directory(path):
    try:
        dirs = os.listdir(path)
        log_action(f"Listed directory: {path}")
        for item in dirs:
            print(item)
        return dirs
    except Exception as e:
        log_action(f"Error listing {path}: {e}")
        print(f"Erreur : {e}")
        return []

def change_directory(path):
    try:
        os.chdir(path)
        log_action(f"Changed directory to: {path}")
    except Exception as e:
        log_action(f"Error changing directory to {path}: {e}")
        print(f"Erreur : {e}")

def rename_item(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        log_action(f"Renamed {old_path} to {new_path}")
    except Exception as e:
        log_action(f"Error renaming {old_path}: {e}")
        print(f"Erreur : {e}")

def add_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        log_action(f"Created directory: {path}")
    except Exception as e:
        log_action(f"Error creating directory {path}: {e}")
        print(f"Erreur : {e}")

def add_file(path, content=""):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        log_action(f"Created file: {path}")
    except Exception as e:
        log_action(f"Error creating file {path}: {e}")
        print(f"Erreur : {e}")

def copy_item(src, dest):
    try:
        if os.path.isdir(src):
            dest = os.path.join(dest, os.path.basename(src))
            shutil.copytree(src, dest)
        else:
            if os.path.isdir(dest):
                dest = os.path.join(dest, os.path.basename(src))
            shutil.copy2(src, dest)
        log_action(f"Copied {src} to {dest}")
    except Exception as e:
        log_action(f"Error copying {src} to {dest}: {e}")
        print(f"Erreur : {e}")

def move_item(src, dest):
    try:
        if os.path.isdir(dest):
            dest = os.path.join(dest, os.path.basename(src))
        shutil.move(src, dest)
        log_action(f"Moved {src} to {dest}")
    except Exception as e:
        log_action(f"Error moving {src} to {dest}: {e}")
        print(f"Erreur : {e}")

def delete_item(path):
    try:
        os.makedirs(TRASH_DIR, exist_ok=True)

        if not os.path.exists(path):
            print("Le chemin n'existe pas.")
            return

        # Génère un nom unique basé sur le timestamp
        timestamp = time.strftime("%Y%m%d%H%M%S")
        base_name = os.path.basename(path)
        trashed_name = f"{timestamp}_{base_name}"
        trashed_path = os.path.join(TRASH_DIR, trashed_name)

        shutil.move(path, trashed_path)

        # Sauvegarde le chemin original pour la restauration
        with open(RESTORE_METADATA, "a") as f:
            f.write(f"{trashed_path}|{path}\n")

        log_action(f"Moved to trash instead of deleting: {path}")
        print(f"{base_name} a été déplacé dans la corbeille.")
    except Exception as e:
        log_action(f"Error moving {path} to trash: {e}")
        print(f"Erreur : {e}")

def restore_item():
    try:
        if not os.path.exists(RESTORE_METADATA):
            print("Aucune sauvegarde disponible.")
            return

        with open(RESTORE_METADATA, "r") as f:
            entries = [line.strip() for line in f if line.strip()]

        if not entries:
            print("La corbeille est vide.")
            return

        print("\n--- Fichiers disponibles pour restauration ---")
        for i, entry in enumerate(entries):
            trashed_path, original_path = entry.split("|")
            print(f"{i + 1}. {os.path.basename(trashed_path)} → {original_path}")

        choice = input("Entrez le numéro du fichier à restaurer (ou rien pour annuler) : ").strip()
        if not choice.isdigit():
            print("Annulé.")
            return

        index = int(choice) - 1
        if index < 0 or index >= len(entries):
            print("Choix invalide.")
            return

        trashed_path, original_path = entries[index].split("|")
        os.makedirs(os.path.dirname(original_path), exist_ok=True)
        shutil.move(trashed_path, original_path)

        # Supprimer l'entrée restaurée
        with open(RESTORE_METADATA, "w") as f:
            for i, entry in enumerate(entries):
                if i != index:
                    f.write(entry + "\n")

        log_action(f"Restored {original_path} from trash")
        print("Restauration effectuée.")
    except Exception as e:
        log_action(f"Error restoring item: {e}")
        print(f"Erreur : {e}")


def get_current_directory():
    try:
        current_dir = os.getcwd()
        log_action(f"Current directory: {current_dir}")
        return current_dir
    except Exception as e:
        log_action(f"Error getting current directory: {e}")
        print(f"Erreur : {e}")
        return None
