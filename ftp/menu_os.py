import os_manager

def menu_os():
    print("--- Menu OS ---")
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
        os_manager.list_directory(path=os_manager.get_current_directory())
    elif choice == "2":
        os_manager.add_directory(input("Nom du dossier à créer : "))
    elif choice == "3":
        os_manager.add_file(input("Nom du fichier à créer : "))
    elif choice == "4":
        old_name = input("Nom actuel : ")
        new_name = input("Nouveau nom : ")
        os_manager.rename_item( old_name, new_name)
    elif choice == "5":
        file_name = input("Nom du fichier ou dossier à supprimer : ")
        if file_name.endswith('/'):
            os_manager.delete_item( file_name)
        else:
            os_manager.delete_item(file_name)
    elif choice == "6":
        source = input("Chemin du fichier ou dossier source : ")
        destination = input("Chemin de destination : ")
        os_manager.copy_item(source, destination)
    elif choice == "7":
        source_path = input("Chemin du fichier ou dossier à déplacer : ")
        destination_path = input("Chemin de destination : ")
        os_manager.move_item(source_path, destination_path)
    elif choice == "8":
        print("Au revoir")
    else:
        print("Choix invalide, veuillez réessayer.")

