import log_manager
from logger import log_action
def menu_log_Sadmin():
    """Menu pour afficher les logs d'activité."""
    while True:
        print("--- Menu Logs d'Activité ---")
        print("1. Afficher les logs d'activité")
        print("2. Afficher les logs d'activité pour Grenoble")
        print("3. Afficher les logs d'activité pour Marseille")
        print("4. Afficher les logs d'activité pour Rennes")
        print("5. Retour au menu principal")
        
        choice = input("Entrez votre choix: ")
        
        if choice == "1":
            print("Affichage des logs d'activité :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs()
            print("--------------------------------------------------")
            log_action("Affichage des logs d'activité")
        elif choice == "2":
            print("Affichage des logs d'activité pour Grenoble :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs_grenoble()
            print("--------------------------------------------------") 
            log_action("Affichage des logs d'activité pour Grenoble")
        elif choice == "3":
            print("Affichage des logs d'activité pour Marseille :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs_marseille()
            print("--------------------------------------------------")
            log_action("Affichage des logs d'activité pour Marseille")
        elif choice == "4":
            print("Affichage des logs d'activité pour Rennes :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs_rennes()
            print("--------------------------------------------------")
            log_action("Affichage des logs d'activité pour Rennes")
        elif choice == "5":
            log_action("Retour au menu principal")
            print("Retour au menu principal")
            break
        else:
            print("Choix invalide, veuillez réessayer.")    

def menu_log_grenoble():
    """Menu pour afficher les logs d'activité."""
    while True:
        print("--- Menu Logs d'Activité ---")
        print("1. Afficher les logs d'activité")
        print("2. Retour au menu principal")
        print("--------------------------------------------------")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            print("Affichage des logs d'activité :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs_grenoble()
            print("--------------------------------------------------")
            log_action("Affichage des logs d'activité")
        elif choice == "2":
            log_action("Retour au menu principal")
            print("Retour au menu principal")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

def menu_log_marseille():
    """Menu pour afficher les logs d'activité."""
    while True:
        print("--- Menu Logs d'Activité ---")
        print("1. Afficher les logs d'activité")
        print("2. Retour au menu principal")
        print("--------------------------------------------------")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            print("Affichage des logs d'activité :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs_marseille()
            print("--------------------------------------------------")
            log_action("Affichage des logs d'activité")
        elif choice == "2":
            log_action("Retour au menu principal")
            print("Retour au menu principal")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

def menu_log_rennes():
    """Menu pour afficher les logs d'activité."""
    while True:
        print("--- Menu Logs d'Activité ---")
        print("1. Afficher les logs d'activité")
        print("2. Retour au menu principal")
        print("--------------------------------------------------")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            print("Affichage des logs d'activité :")
            print("--------------------------------------------------")
            log_manager.afficher_f_logs_rennes()
            print("--------------------------------------------------")
            log_action("Affichage des logs d'activité")
        elif choice == "2":
            log_action("Retour au menu principal")
            print("Retour au menu principal")
            break
        else:
            print("Choix invalide, veuillez réessayer.")