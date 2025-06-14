import os
import shutil
from logger import log_action
def list_directory(path):
    try:
        dirs = os.listdir(path)
        log_action(f"Listed directory: {path}")
        return dirs
    except Exception as e:
        log_action(f"Error listing {path}: {e}")
        return []

def change_directory(path):
    try:
        os.chdir(path)
        log_action(f"Changed directory to: {path}")
    except Exception as e:
        log_action(f"Error changing directory to {path}: {e}")

def rename_item(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        log_action(f"Renamed {old_path} to {new_path}")
    except Exception as e:
        log_action(f"Error renaming {old_path}: {e}")

def add_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        log_action(f"Created directory: {path}")
    except Exception as e:
        log_action(f"Error creating directory {path}: {e}")

def add_file(path, content=""):
    try:
        with open(path, "w") as f:
            f.write(content)
        log_action(f"Created file: {path}")
    except Exception as e:
        log_action(f"Error creating file {path}: {e}")

def copy_item(src, dest):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
        log_action(f"Copied {src} to {dest}")
    except Exception as e:
        log_action(f"Error copying {src} to {dest}: {e}")

def move_item(src, dest):
    try:
        shutil.move(src, dest)
        log_action(f"Moved {src} to {dest}")
    except Exception as e:
        log_action(f"Error moving {src} to {dest}: {e}")

def delete_item(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        log_action(f"Deleted {path}")
    except Exception as e:
        log_action(f"Error deleting {path}: {e}")