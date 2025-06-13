from ftplib import FTP
import os
from config import FTP_HOST, FTP_PORT, FTP_USER, FTP_PASS
from logger import log_action, setup_logger

def connect_ftp():
    setup_logger()  # Ensure logger is set up
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    log_action(f"Connexionn reussi avec l'FTP {FTP_HOST}:{FTP_PORT} en tant que {FTP_USER}")
    return ftp

def list_dossier(ftp):
    print("Contenu du répertoire distant :")
    ftp.dir()

def add_dossier(ftp, fichier):
    try:
        ftp.mkd(fichier)
        log_action(f"Created directory: {fichier} on FTP.")
    except Exception as e:
        log_action(f"Error creating directory {fichier}: {e}")
        print(f"Erreur lors de la création du dossier : {e}")

def add_file(ftp, fichier):
    with open(fichier, 'w') as f:
        pass
    try:
        with open(fichier, 'rb') as f:
            ftp.storbinary(f"STOR {fichier}", f)
            log_action(f"Uploaded file: {fichier} to FTP.")
    except Exception as e:
        log_action(f"Error uploading file {fichier}: {e}")
        print(f"Erreur lors de l'envoi du fichier : {e}")
    os.remove(fichier)  # Remove local file after upload


def change_dossier(ftp, path):
    try:
        ftp.cwd(path)
        log_action(f"Changed directory to: {path} on FTP.")
    except Exception as e:
        log_action(f"Error changing directory to {path}: {e}")
        print(f"Erreur lors du changement de dossier : {e}")

def del_dossier(ftp, dossier):
    try:
        ftp.rmd(dossier)
        log_action(f"Deleted directory: {dossier} on FTP.")
    except Exception as e:
        log_action(f"Error deleting directory {dossier}: {e}")
        print(f"Erreur lors de la suppression du dossier : {e}")

def del_file(ftp, fichier):
    try:
        ftp.delete(fichier)
        log_action(f"Deleted file: {fichier} on FTP.")
    except Exception as e:
        log_action(f"Error deleting file {fichier}: {e}")
        print(f"Erreur lors de la suppression du fichier : {e}")

def list_files(ftp):
    try:
        files = ftp.nlst()
        log_action("Listed files in current directory on FTP.")
        return files
    except Exception as e:
        log_action(f"Error listing files: {e}")
        return []
    
def is_directory(ftp, name):
    current = ftp.pwd()
    try:
        ftp.cwd(name)
        ftp.cwd(current)
        return True
    except error_perm:
        return False

def copy_folder(ftp, source, destination):
    folder_name = source.strip("/").split("/")[-1]
    target_dir = f"{destination.rstrip('/')}/{folder_name}"

    # Créer le dossier destination
    try:
        ftp.mkd(target_dir)
        log_action(f"Dossier créé : {target_dir}")
    except error_perm as e:
        log_action(f"Dossier {target_dir} existant ou erreur : {e}")

    # Accéder au dossier source
    try:
        ftp.cwd(source)
        items = ftp.nlst()
    except Exception as e:
        log_action(f"Erreur d'accès à {source} : {e}")
        return

    for item in items:
        # Vérifier si c'est un dossier
        if is_directory(ftp, item):
            log_action(f"Ignoré (dossier) : {item}")
            continue

        # Télécharger même les fichiers vides
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                ftp.retrbinary(f"RETR {item}", tmp_file.write)
                temp_path = tmp_file.name
        except Exception as e:
            log_action(f"Erreur RETR {item} : {e}")
            continue

        # Aller dans le bon dossier de destination
        try:
            ftp.cwd(target_dir)
            with open(temp_path, "rb") as f:
                ftp.storbinary(f"STOR {item}", f)
            log_action(f"Copié : {item} → {target_dir}")
        except Exception as e:
            log_action(f"Erreur STOR {item} → {target_dir} : {e}")
        finally:
            os.remove(temp_path)

        # Revenir dans le dossier source
        ftp.cwd(source)

    ftp.cwd("..")

def rename_ftp(ftp, old_name, new_name):
    try:
        ftp.rename(old_name, new_name)
        log_action(f"Renamed {old_name} to {new_name} on FTP.")
    except Exception as e:
        log_action(f"Error renaming {old_name} to {new_name}: {e}")

def upload_file(ftp, local_file, remote_path):
    with open(local_file, 'rb') as f:
        ftp.storbinary(f"STOR {remote_path}", f)
        log_action(f"Uploaded {local_file} to {remote_path} on FTP.")

def ensure_ftp_dir(ftp, path):
    try:
        ftp.mkd(path)
    except Exception:
        pass  # Already exists

def upload_audit_backup(local_file, region, client):
    ftp = connect_ftp()
    remote_dir = f"/backups/{region}/{client}"
    ensure_ftp_dir(ftp, f"/backups/{region}")
    ensure_ftp_dir(ftp, remote_dir)

    filename = os.path.basename(local_file)
    remote_path = f"{remote_dir}/{filename}"
    upload_file(ftp, local_file, remote_path)
    ftp.quit()

def upload_file(ftp, local_file, remote_file_name=None, remote_path=""):
    try:
        if not remote_file_name:
            remote_file_name = os.path.basename(local_file)
        remote_full_path = f"{remote_path}/{remote_file_name}".strip("/")
        with open(local_file, 'rb') as f:
            ftp.storbinary(f"STOR {remote_full_path}", f)
        log_action(f"Uploaded {local_file} to {remote_full_path} on FTP.")
        print(f"Fichier envoyé : {local_file} → {remote_full_path}")
    except Exception as e:
        print(f"Erreur lors de l'upload : {e}")
        log_action(f"Erreur upload de {local_file} : {e}")

def download_file(ftp, local_path, remote_file_name):
    try:
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        local_full_path = os.path.join(local_path, remote_file_name)
        with open(local_full_path, 'wb') as f:
            ftp.retrbinary(f"RETR {remote_file_name}", f.write)
        log_action(f"Téléchargé {remote_file_name} vers {local_full_path} depuis FTP.")
        print(f"Fichier téléchargé : {remote_file_name} → {local_full_path}")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}")
        log_action(f"Erreur téléchargement de {remote_file_name} : {e}")

def move_file(ftp, source_path, destination_path):
    try:
        ftp.rename(source_path, destination_path)
        log_action(f"Déplacé : {source_path} → {destination_path}")
        print(f"Fichier déplacé de {source_path} vers {destination_path}")
    except Exception as e:
        print(f"Erreur lors du déplacement : {e}")
        log_action(f"Erreur déplacement {source_path} → {destination_path} : {e}")

import os

def move_directory(ftp, src_path, dest_path):
    try:
        # Étape 1 : créer le dossier de destination
        try:
            ftp.mkd(dest_path)
        except Exception:
            pass  # Le dossier existe déjà
        # Étape 2 : naviguer dans le dossier source
        ftp.cwd(src_path)
        items = ftp.nlst()
        for item in items:
            # Vérifie si c’est un fichier ou un dossier (très basique)
            try:
                ftp.cwd(item)  # si on peut entrer, c’est un dossier
                ftp.cwd('..')  # revenir en arrière
                move_directory(ftp, f"{src_path}/{item}", f"{dest_path}/{item}")  # appel récursif
                ftp.rmd(f"{src_path}/{item}")  # suppression du dossier vide
            except Exception:
                # C’est un fichier
                with open("temp_file", "wb") as f:
                    ftp.retrbinary(f"RETR {src_path}/{item}", f.write)
                with open("temp_file", "rb") as f:
                    ftp.storbinary(f"STOR {dest_path}/{item}", f)
                ftp.delete(f"{src_path}/{item}")

        ftp.cwd('..')  # revenir avant suppression
        ftp.rmd(src_path)
        print(f"Dossier déplacé de {src_path} vers {dest_path}")
    except Exception as e:
        print(f"Erreur lors du déplacement : {e}")


