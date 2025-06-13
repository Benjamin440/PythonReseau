import file_manager
import ftp_manager


def menu_super_admin_ftp():

    ftp = ftp_manager.connect_ftp()
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
        ftp_manager.list_dossier(ftp)
    elif choice == "2":
        file_manager.change_directory(fichier)
    elif choice == "3":
        print("Entrez le nom du fichier ou dossier à renommer:")
        fichier = input("Nom du fichier ou dossier: ")
        ftp_manager.rename_ftp(fichier)
    elif choice == "4":
        file_manager.add_file(fichier)
    elif choice == "5":
        print("1. Créer un dossier")
        print("2. Créer un fichier")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            file_manager.add_directory(fichier)
        elif choice == "2":
            file_manager.add_file(fichier)
    elif choice == "6":
        file_manager.copy_item(fichier)
    elif choice == "7":
        file_manager.move_item(fichier)
    elif choice == "8":
        file_manager.delete_item(fichier)
    elif choice == "9":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_super_admin_ftp()
