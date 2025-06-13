import ftp_manager
import menu_scanner
import menu_scan_reseau
from logger import log_action

def menu_general():
        print("--- Menu Général ---")
        print("1. Scan de port")
        print("2. Scan réseau")
        print("3. Gérer les fichiers FTP")
        print("4. Quitter")
        choice = input("Entrez votre choix: ")
        
        if choice == "1":
            menu_scanner.scan()
        elif choice == "2":
            menu_scan_reseau.scan()
        elif choice == "3":
            menu_super_admin_ftp()
        elif choice == "4":
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
        print("4. Upload ou Download des dossiers ou fichiers")
        print("5. Créer des dossiers ou fichiers")
        print("6. Copier des dossiers ou fichiers")
        print("7. Déplacer des dossiers ou fichiers")
        print("8. Supprimer des dossiers ou fichiers")
        print("9.Quitter")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            ## Lister les dossiers
            print(f"\nRépertoire courant : {ftp.pwd()}")
            ftp_manager.list_dossier(ftp)
        elif choice == "2":
            while True:
                ftp_manager.list_dossier(ftp)
                print(f"\nRépertoire courant : {ftp.pwd()}")
                print("\nEntrez le nom du dossier à ouvrir :")
                print("Tapez '..' pour revenir au dossier parent")
                print("Tapez '/' pour revenir à la racine")
                print("Tapez 'menu' pour revenir au menu principal")
                

                dossier = input("Nom du dossier : ").strip()

                if dossier == "menu":
                    break  # sortir de la boucle interne et revenir au menu principal
                elif dossier == "..":
                    try:
                        ftp.cwd("..")
                        print(f"Retour au dossier parent : {ftp.pwd()}")
                        log_action(f"Retour au dossier parent : {ftp.pwd()}")
                    except Exception as e:
                        print(f"Impossible de revenir en arrière : {e}")
                        log_action(f"Erreur lors du retour en arrière : {e}")
                elif dossier == "/":
                    try:
                        ftp.cwd("/")
                        print(f"Retour à la racine : {ftp.pwd()}")
                        log_action(f"Retour à la racine : {ftp.pwd()}")
                    except Exception as e:
                        print(f"Impossible d'aller à la racine : {e}")
                        log_action(f"Erreur retour racine : {e}")
                elif dossier:
                    try:
                        ftp_manager.change_dossier(ftp, dossier)
                        print(f"Changement de dossier réussi : {ftp.pwd()}")
                    except Exception as e:
                        print(f"Erreur de navigation : {e}")
                else:
                    print("⚠ Veuillez entrer un nom de dossier valide.")
        elif choice == "3":
            old = input("Nom actuel : ")
            new = input("Nouveau nom : ")
            if old and new:
                ftp_manager.rename_ftp(ftp, old, new)
            else:
                print(" Les deux noms doivent être renseignés.")
        elif choice == "4":
            print("1. Upload un fichier ou dossier")
            print("2. Download un fichier ou dossier")
            choice = input("Entrez votre choix: ")
            if choice == "1":
                print(f"\nRépertoire courant : {ftp.pwd()}")
                local_path = input("Entrez le chemin local du fichier à ajouter : ")
                remote_file_name = input("Entrez le nom du fichier distant : ")
                remote_path = input("Entrez le chemin distant (laisser vide pour le répertoire courant) : ")
                ftp_manager.upload_file(ftp, local_path, remote_file_name, remote_path)
            elif choice == "2":
                print(f"\nRépertoire courant : {ftp.pwd()}")
                local_path = input("Entrez le chemin local où télécharger le fichier : ")
                remote_file_name = input("Entrez le nom du fichier distant à télécharger : ")
                ftp_manager.download_file(ftp, local_path, remote_file_name)
        elif choice == "5":
            print("1. Créer un dossier")
            print("2. Créer un fichier")
            choice = input("Entrez votre choix: ")
            if choice == "1":
                print(f"\nRépertoire courant : {ftp.pwd()}")
                fichier = input("Nom du dossier à créer : ")
                if not fichier.strip():
                    print(" Le nom du dossier ne peut pas être vide.")
                    continue
                ftp_manager.add_dossier(ftp, fichier)
                print(f" Dossier '{fichier}' créé avec succès.")
            elif choice == "2":
                fichier = input("Nom du fichier à créer : ")
                if not fichier.strip():
                    print(" Le nom du fichier ne peut pas être vide.")
                    continue
                ftp_manager.add_file(ftp, fichier)
                print(f" Fichier '{fichier}' créé avec succès.")
        elif choice == "6":
            source = input("Entrez le chemin du fichier ou dossier source : ")
            destination = input("Entrez le chemin de destination : ")
            ftp_manager.copy_folder(ftp, source, destination)
        elif choice == "7":
            print(f"\nRépertoire courant : {ftp.pwd()}")
            source_path = input("Entrez le chemin du fichier ou dossier à déplacer : ")
            destination_path = input("Entrez le chemin de destination : ")
            if not source_path.strip() or not destination_path.strip():
                print(" Les chemins source et destination ne peuvent pas être vides.")
                continue
            ftp_manager.move_file(ftp, source_path, destination_path)
        elif choice == "8":
            print("1. Supprimer un dossier")
            print("2. Supprimer un fichier")
            choice = input("Entrez votre choix: ")
            if choice == "1":
                fichier = input("Nom du dossier à supprimer : ")
                if not fichier.strip():
                    print(" Le nom du dossier ne peut pas être vide.")
                    continue
                ftp_manager.del_dossier(ftp, fichier)
            elif choice == "2":
                fichier = input("Nom du fichier à supprimer avec extension : ")
                if not fichier.strip():
                    print(" Le nom du fichier ne peut pas être vide.")
                    continue
                ftp_manager.del_file(ftp, fichier)
        elif choice == "9":
            print("Au revoir")
            ftp.quit()
            break
        else:
            print("Choix invalide")
            menu_super_admin_ftp()
