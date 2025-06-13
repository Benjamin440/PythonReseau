import scanner_reseau
def scan():
    print("--- Menu Scan Réseau ---")
    print("1. Scanner un réseau")
    print("2. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        scanner_reseau.main()
    elif choice == "2":
        print("Retour au menu principal.")