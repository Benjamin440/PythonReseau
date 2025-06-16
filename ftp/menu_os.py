import os_manager

def menu_os():
    os_manager.change_directory(r"C:/New_Tech")  
    while True:
        print("\n--- Menu OS ---")
        print(f"Répertoire actuel : {os_manager.get_current_directory()}")

        print("1. Lister les fichiers et dossiers")
        print("2. Changer de répertoire")
        print("3. Créer un dossier")
        print("4. Créer un fichier")
        print("5. Renommer un fichier ou dossier")
        print("6. Supprimer un fichier ou dossier")
        print("7. Copier un fichier ou dossier")
        print("8. Déplacer un fichier ou dossier")
        print("9. Quitter")
        
        choice = input("Entrez votre choix: ").strip()

        if choice == "1":
            path = input("Chemin à lister (laisser vide pour le dossier actuel) : ").strip()
            if not path:
                path = os_manager.get_current_directory()
            os_manager.list_directory(path)

        elif choice == "2":
            path = input("Entrez le chemin du dossier : ")
            os_manager.change_directory(path)

        elif choice == "3":
            path = input("Chemin du dossier à créer : ")
            os_manager.add_directory(path)

        elif choice == "4":
            path = input("Chemin du fichier à créer : ")
            content = input("Contenu (laisser vide si aucun) : ")
            os_manager.add_file(path, content)

        elif choice == "5":
            old_name = input("Nom actuel : ")
            new_name = input("Nouveau nom : ")
            os_manager.rename_item(old_name, new_name)

        elif choice == "6":
            path = input("Nom du fichier ou dossier à supprimer : ")
            os_manager.delete_item(path)

        elif choice == "7":
            source = input("Chemin du fichier ou dossier source : ")
            destination = input("Chemin de destination : ")
            os_manager.copy_item(source, destination)

        elif choice == "8":
            source_path = input("Chemin du fichier ou dossier à déplacer : ")
            destination_path = input("Chemin de destination : ")
            os_manager.move_item(source_path, destination_path)

        elif choice == "9":
            print("Au revoir")
            break

        else:
            print("Choix invalide, veuillez réessayer.")
