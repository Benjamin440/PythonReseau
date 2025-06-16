import os
from config import ROOT_DIR, REGIONS, FTP_USER, FTP_PASS
from logger import log_action, setup_logger, setup_logger_grenoble, setup_logger_marseille, setup_logger_rennes
import menu

def main():
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
    if FTP_USER == "admin":
        print("Bienvenue, Super Admin!")
        menu.menu_super_admin()
    else:
        menu.menu_admin()

    # print("=== Gestion Automatisée du SGF ===")
    # Exemple d'opérations automatiques
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

