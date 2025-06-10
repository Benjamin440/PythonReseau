import Crud
import Authent
import getpass
def main ():
    while True :
        print("Bienvenue sur l'AD")
        print("1. Connexion")
        print("2. Quitter")
        choix = input("Que voulez-vous faire ? ")

        if choix == "1":
            login = input("Entrez votre login: ")
            password = getpass.getpass("Entrez votre mot de passe: ")
            if Authent.authent(login, password) == True: ##Utilisation de getpass pour cacher l'écriture du mdp
                Authent.verify_role(login) ##Appel de la fonction verify_role 
            else:
                main()
        elif choix == "2":

            print("Au revoir")
            break
            exit()

main()