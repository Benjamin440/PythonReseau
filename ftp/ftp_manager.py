from ftplib import FTP
from config import FTP_HOST, FTP_PORT, FTP_USER, FTP_PASS
from logger import log_action
from logger import setup_logger

    
def connect_ftp():
    setup_logger()
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    log_action(f"Connexionn reussi avec l'FTP {FTP_HOST}:{FTP_PORT} en tant que {FTP_USER}")
    print("✅ Connected to FTP server.")
    return ftp

def list_dossier(ftp):
    print("📁 Contenu du répertoire distant :")
    ftp.dir()

    

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


connect_ftp()  # Ensure connection is established for the module