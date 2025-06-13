import file_manager
import ftp_manager
import menu_scanner
from logger import log_action

def menu_general():
        print("--- Menu Général ---")
        print("1. Scan réseau et scan de port")
        print("2. Gérer les fichiers FTP")
        print("3. Quitter")
        choice = input("Entrez votre choix: ")
        
        if choice == "1":
            menu_scanner.scan()
        elif choice == "2":
            menu_super_admin_ftp()
        elif choice == "3":
            print("Au revoir")
        else:
            print("Choix invalide, veuillez réessayer.")
            menu_general()


def menu_super_admin_ftp():
    ftp = ftp_manager.connect_ftp()

    while True:
        print("--- Menu Super Admin ---")
        print("1. Lister les dossier")## Naviguer dans les dossiers
        print("2. Se déplacer dans un dossier")##Gérer les chemins des dossiers
        print("3. Renommer des dossier ou fichiers")
        print("4. Ajouter des dossiers ou fichiers")
        print("5. Créer des dossiers ou fichiers")
        print("6. Copier des dossiers ou fichiers")
        print("7.Déplacer des dossiers ou fichiers")
        print("8. Supprimer des dossiers ou fichiers")
        print("9.Quitter")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            ## Lister les dossiers
            print(f"\nRépertoire courant : {ftp.pwd()}")
            ftp_manager.list_dossier(ftp)
        elif choice == "2":
            ftp_manager.list_dossier(ftp)
            print(f"\nRépertoire courant : {ftp.pwd()}")
            dossier = input("Nom du dossier à ouvrir (ou '..' pour revenir en arrière) : ")
            if dossier.strip():
                if dossier.strip() == "..":
                    try:
                        ftp.cwd("..")
                        print(f" Revenu au dossier parent : {ftp.pwd()}")
                        log_action(f"Revenu au dossier parent : {ftp.pwd()}")
                    except Exception as e:
                        print(f"Impossible de revenir en arrière : {e}")
                        log_action(f"Erreur lors du retour en arrière : {e}")
                else:
                    ftp_manager.change_dossier(ftp, dossier.strip())
                    print(f" Changement de dossier réussi : {ftp.pwd()}")
        elif choice == "3":
            old = input("Nom actuel : ")
            new = input("Nouveau nom : ")
            if old and new:
                ftp_manager.rename_ftp(ftp, old, new)
            else:
                print(" Les deux noms doivent être renseignés.")
        elif choice == "4":
            ftp_manager.add_file(ftp, fichier)
        elif choice == "5":
            print("1. Créer un dossier")
            print("2. Créer un fichier")
            choice = input("Entrez votre choix: ")
            if choice == "1":
                ftp_manager.add_dossier(ftp, fichier)
            elif choice == "2":
                ftp_manager.add_file(ftp, fichier)
        elif choice == "6":
            ftp_manager.copy_item(ftp, fichier)
        elif choice == "7":
            ftp_manager.change_dossier(ftp, fichier)
        elif choice == "8":
            ftp_manager.delete_item(ftp, fichier)
        elif choice == "9":
            print("Au revoir")
            ftp.quit()
            break
        else:
            print("Choix invalide")
            menu_super_admin_ftp()
