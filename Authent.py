import SqlRequest
from User import User
import Crud
import getpass

def authent(login, password):
    cpt = 0
    password = User.hash_password(None, password)
    res = SqlRequest.select_user(login)
    if res and password == res[0][7]:
        print("Vous êtes connecté")
        return True
    else:
        while cpt < 2: ## Utilisation d'un compteur pour vérifier 3 fois le login et le mot de passe
            print("Mauvais nom d'utilisateur ou mot de passe")
            login = input("Entrez votre login: ")
            password = getpass.getpass("Entrez votre mot de passe: ")
            password = User.hash_password(None, password)
            res = SqlRequest.select_user(login)
            if res and password == res[0][7]:
                print("Vous êtes connecté")
                return True
            cpt += 1

def verify_role(login): ## Fonction pour vérifier le role de l'utilisateur entre utilisateur, admin et super_admin
    res = SqlRequest.select_user(login) 
    ville = res[0][3]
    if res[0][8] == "UTILISATEUR":
        Crud.menu_utilisateur()
    elif res[0][8] == "ADMIN":
        Crud.menu_admin(ville)
    else:
        Crud.menu_super_admin(ville)


