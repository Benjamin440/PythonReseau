import os
import shutil
from logger import log_action

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
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        log_action(f"Deleted {path}")
    except Exception as e:
        log_action(f"Error deleting {path}: {e}")
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
