import os
from config import ROOT_DIR, REGIONS
import menu_ftp

def main():
    menu_ftp.menu_general()



    # print("=== Gestion Automatisée du SGF ===")
    # # Exemple d'opérations automatiques
    # for region in REGIONS:
    #     region_path = os.path.join(ROOT_DIR, region)
    #     clients = fm.list_directory(region_path)
    #     for client in clients:
    #         client_path = os.path.join(region_path, client)
    #         files = fm.list_directory(client_path)
    #         for f in files:
    #             if f.startswith("audit."):
    #                 local_file = os.path.join(client_path, f)
    #                 ftp.upload_audit_backup(local_file, region, client)


if __name__ == "__main__":
    main()

