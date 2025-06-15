import os_manager

def menu_os():
    print("--- Menu Super Admin OS ---")
    print("1. Lister les fichiers et dossiers")
    print("2. Créer un dossier")
    print("3. Créer un fichier")
    print("4. Renommer un fichier ou dossier")
    print("5. Supprimer un fichier ou dossier")
    print("6. Copier un fichier ou dossier")
    print("7. Déplacer un fichier ou dossier")
    print("8. Quitter")
    
    choice = input("Entrez votre choix: ")
    
    if choice == "1":
        os_manager.list_directory(ftp_manager.connect_ftp())
    elif choice == "2":
        os_manager.create_directory(os_manager.connect_ftp(), input("Nom du dossier à créer : "))
    elif choice == "3":
        os_manager.add_file(os_manager.connect_ftp(), input("Nom du fichier à créer : "))
    elif choice == "4":
        old_name = input("Nom actuel : ")
        new_name = input("Nouveau nom : ")
        os_manager.rename_file(os_manager.connect_ftp(), old_name, new_name)
    elif choice == "5":
        file_name = input("Nom du fichier ou dossier à supprimer : ")
        if file_name.endswith('/'):
            os_manager.delete_directory(os_manager.connect_ftp(), file_name)
        else:
            os_manager.del_file(os_manager.connect_ftp(), file_name)
    elif choice == "6":
        source = input("Chemin du fichier ou dossier source : ")
        destination = input("Chemin de destination : ")
        os_manager.copy_folder(os_manager.connect_ftp(), source, destination)
    elif choice == "7":
        source_path = input("Chemin du fichier ou dossier à déplacer : ")
        destination_path = input("Chemin de destination : ")
        os_manager.move_file(os_manager.connect_ftp(), source_path, destination_path)
    elif choice == "8":
        print("Au revoir")
    else:
        print("Choix invalide, veuillez réessayer.")

