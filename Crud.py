from User import User as U
from User import PHospitalier as PH
from User import Patient as P
import SqlRequest as SqlRequest
import re

### Constantes ###
AJOUT_USER = "Ajout d'un Utilisateur"
AJOUT_OK = "Utilisateur ajouté"
NOM_USER = "Entrez le nom : "
PRENOM_USER = "Entrez le prénom : "
VILLE_USER = "Choissisez une ville PARIS | RENNES | STRASBOURG | GRENOBLE | NANTES : "
NUMERO_USER = "Entrez le numéro de téléphone: "
ROLE_USER = "Entrez le role : "
SERVICE_USER = "Entrez le service : "
S_SOCIAL_USER = "Entrez le numéro de sécurité social : "
LOGIN_USER = "Entrez le login : "


### Ajout User ###
def add_user():
    print(AJOUT_USER)
    nom = input(NOM_USER).upper()
    prenom = input(PRENOM_USER)
    ville = input(VILLE_USER).upper()
    numero = input(NUMERO_USER)
    role = input(ROLE_USER)
    user = U(" ", nom, prenom, ville, numero, role, "", "", "", "")

    # Génération de l'email et du login
    user.gen_email()
    user.gen_login()
    # Génération du mot de passe
    passwordv = user.gen_password()
    if not passwordv:
        raise ValueError("Erreur : le mot de passe généré est vide ou None")
    hashed_password = user.hash_password(passwordv)
    if not hashed_password:
        raise ValueError("Erreur : le hashage du mot de passe a échoué")
    # Stockage du mot de passe hashé et du mot de passe en clair
    user.set_password(hashed_password)
    user.set_password_clear(passwordv)
    # Attribution du matricule et insertion en base
    user.set_mat_user(SqlRequest.countmatricule() + 1)
    SqlRequest.insert_user(user)
    print(AJOUT_OK)
    return user

### Ajout User PH ###
def add_user_ph(admin_ville):
    villes_autorisees = {"PARIS", "RENNES", "STRASBOURG", "GRENOBLE", "NANTES"}
    if admin_ville.upper() not in villes_autorisees:
        print("Vous n'avez pas l'autorisation de créer des utilisateurs pour cette ville.")
        return None
    print(AJOUT_USER)
    matricule = " "
    nom = input(NOM_USER).upper()
    prenom = input(PRENOM_USER)
    # Si l'admin est de Paris, il peut choisir la ville, sinon il est limité à sa propre ville
    if admin_ville.upper() == "PARIS":
        ville = input(VILLE_USER).upper()  # Admin de Paris peut choisir la ville
        if ville not in villes_autorisees:
            print(f"Vous ne pouvez créer des utilisateurs que pour les villes suivantes : {', '.join(villes_autorisees)}.")
            return None
    else:
        ville = admin_ville.upper()  # Admin des autres villes est restreint à sa propre ville
    numero = input(NUMERO_USER)
    service = input(SERVICE_USER)
    ph = PH(matricule, nom, prenom, ville, numero, "UTILISATEUR",service , "", "", "", "" )

    # Génération de l'email et du login
    ph.gen_email()
    ph.gen_login()

    # Génération du mot de passe
    passwordv = ph.gen_password()
    if not passwordv:
        raise ValueError("Erreur : le mot de passe généré est vide ou None")
    hashed_password = ph.hash_password(passwordv)
    if not hashed_password:
        raise ValueError("Erreur : le hashage du mot de passe a échoué")
    # Stockage du mot de passe hashé et du mot de passe en clair
    ph.set_password(hashed_password)
    ph.set_password_clear(passwordv)
    
    ph.set_mat_user(SqlRequest.countmatricule() + 1)
    SqlRequest.insert_user_ph(ph)
    print(AJOUT_OK)
    return ph

### Ajout User Patient ###
def add_user_patient(admin_ville):
    villes_autorisees = {"PARIS", "RENNES", "STRASBOURG", "GRENOBLE", "NANTES"}
    if admin_ville.upper() not in villes_autorisees:
        print("Vous n'avez pas l'autorisation de créer des utilisateurs pour cette ville.")
        return None
    print(AJOUT_USER)
    matricule = " "
    nom = input(NOM_USER).upper()
    prenom = input(PRENOM_USER)
    # Si l'admin est de Paris, il peut choisir la ville, sinon il est limité à sa propre ville
    if admin_ville.upper() == "PARIS":
        ville = input(VILLE_USER).upper()  # Admin de Paris peut choisir la ville
        if ville not in villes_autorisees:
            print(f"Vous ne pouvez créer des utilisateurs que pour les villes suivantes : {', '.join(villes_autorisees)}.")
            return None
    else:
        ville = admin_ville.upper()  # Admin des autres villes est restreint à sa propre ville
    numero = input(NUMERO_USER)
    s_social = input(S_SOCIAL_USER)
    role = "UTILISATEUR"
    password = input(PASSWORD_USER)
    patient = P(matricule,nom, prenom, ville, numero, s_social, role, password)
    patient.set_mat_user(SqlRequest.countmatricule() + 1)
    SqlRequest.insert_user_patient(patient)
    print(AJOUT_OK)
    return patient

def verify_ville(ville):
    villes_autorisees = {"PARIS", "RENNES", "STRASBOURG", "GRENOBLE", "NANTES"}
    if not ville:
        raise ValueError("La ville ne peut pas être vide")
    if ville.upper() not in villes_autorisees:
        raise ValueError("La ville doit être parmi les suivantes : PARIS, RENNES, STRASBOURG, GRENOBLE, NANTES")
    return ville.upper()

def verify_service(service):
    service_autorisees = {"URGENCE", "NEUROLOGIE", "CARDIOLOGIE"}
    if not service:
        raise ValueError("Le service ne peut pas être vide")
    if service.upper() not in service_autorisees:
        raise ValueError("Le service doit être parmi les suivants : URGENCE, NEUROLOGIE, CARDIOLOG")
    return service

### Affichage User ###
def afficher_user_ville(ville):
    try:
        ville = verify_ville(ville)
        res2 = SqlRequest.select_ville(ville)
        if not res2:
            print(f"Aucun utilisateur trouvé pour la ville {ville}.")
            return
        print(f"Liste des utilisateurs pour la ville {ville} :")
        for row in res2:
            print(row) 
    except ValueError as e:
        print(f"Erreur : {e}")

def afficher_user_service(service):
    try:
        service = verify_service(service)
        res2 = SqlRequest.select_service(service)
        if not res2:
            print(f"Aucun utilisateur trouvé pour le service {service}.")
            return
        print(f"Liste des utilisateurs pour le service {service} :")
        for row in res2:
            print(row)
    except ValueError as e:
        print(f"Erreur : {e}")

def afficher_user():
    login = input(LOGIN_USER)
    res = SqlRequest.select_user2(login) ## Récupération des informations de l'utilisateur via la requete SQL
    if res:
        print("Utilisateur trouvé")
        print("Nom: ", res[0][0])
        print("Prénom: ", res[0][1])
        print("Ville: ", res[0][2])
        print("Numéro: ", res[0][3])
        print("Email: ", res[0][4])
        print("Role: ", res[0][5])
        if res[0][7] is not None:
            print("Service: ", res[0][7])
        elif res[0][6] is not None:
            print("Numéro de sécurité social: ", res[0][6])
    else:
        print("Utilisateur non trouvé")

### Suppression User ###
def delete_user():
    login = input(LOGIN_USER)
    res = SqlRequest.select_user(login)
    if res:
        print("1. Oui")
        print("2. Non")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            SqlRequest.delete_user(res[0][0]) ## Suppression de l'utilisateur via la requete SQL
            print("Utilisateur supprimé")
        elif choice == "2":
            print("Suppression annulée")
        else:
            print("Choix invalide")
            delete_user()
    else:
        print("Utilisateur non trouvé")

### Modification User ###
def modify_user():
    login = input(LOGIN_USER)
    res = SqlRequest.select_user(login)
    if res:
        print("Modification de l'utilisateur")
        print("1. Nom")
        print("2. Prénom")
        print("3. Ville")
        print("4. Numéro")
        print("5. Email")
        print("6. Login")
        print("7. Password")
        print("8. Role")
        if res[0][10] is not None:
            print("9. Service")
        elif res[0][9] is not None:
            print("9. Numéro de sécurité social")
        print("10. Retour")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            nom = input("Entrez le nouveau nom: ")
            SqlRequest.update_user(res[0][0], "nom", nom)
        elif choice == "2":
            prenom = input("Entrez le nouveau prénom: ")
            SqlRequest.update_user(res[0][0], "prenom", prenom)
        elif choice == "3":
            ville = input("Entrez la nouvelle ville: ")
            SqlRequest.update_user(res[0][0], "ville", ville)
        elif choice == "4":
            numero = input("Entrez le nouveau numéro: ")
            SqlRequest.update_user(res[0][0], "numero", numero)
        elif choice == "5":
            email = input("Entrez le nouvel email: ")
            SqlRequest.update_user(res[0][0], "email", email)
        elif choice == "6":
            login = input("Entrez le nouveau login: ")
            SqlRequest.update_user(res[0][0], "login", login)
        elif choice == "7":
            password = input("Entrez le nouveau mot de passe: ")
            SqlRequest.update_user(res[0][0], "password", password)
        elif choice == "8":
            role = input("Entrez le nouveau role: ")
            SqlRequest.update_user(res[0][0], "role", role)
        elif choice == "9":
            if res[0][10] is not None:
                service = input("Entrez le nouveau service: ")
                SqlRequest.update_user(res[0][0], "service", service)
            elif res[0][9] is not None:
                s_social = input("Entrez le nouveau numéro de sécurité social: ")
                SqlRequest.update_user(res[0][0], "s_social", s_social)

### Menu User ###
def menu_super_admin(ville):
    print("--- Menu Super Admin ---")
    print("1. Ajouter un utilisateur")
    print("2. Modifier un utilisateur")
    print("3. Afficher un utilisateur")
    print("4. Afficher un utilisateur via le service")
    print("5. Supprimer un utilisateur")
    print("6. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        print("1. Utilisateur")
        print("2. Personnel Hospitalier")
        print("3. Patient")
        print("4. Retour Menu")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            add_user_ph(ville)
        elif choice == "3":
            add_user_patient(ville)
        elif choice == "4":
            print("Au revoir")
        else:
            print("Choix invalide")
            menu_super_admin()
    elif choice == "2":
        modify_user()
    elif choice == "3":
        afficher_user()
    elif choice == "4":
        afficher_user_service(input("Entrez le service : "))
    elif choice == "5":
        delete_user()
    elif choice == "6":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_super_admin()

def menu_admin(ville):
    print("--- Menu Admin ---")
    print("1. Ajouter un utilisateur")
    print("2. Modifier un utilisateur")
    print("3. Afficher un utilisateur")
    print ("4. Supprimer un utilisateur")
    print("5. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        print("1. Personnel Hospitalier")
        print("2. Patient")
        print("3. Retour Menu")
        choice = input("Entrez votre choix: ")
        if choice == "1":
            add_user_ph(ville) ## Ajout d'un utilisateur PH
        elif choice == "2":
            add_user_patient(ville) ## Ajout d'un patient
        elif choice == "3":
            print("Au revoir")
        else:
            print("Choix invalide")
            menu_admin() ## Retour au menu admin
    elif choice == "2":
        modify_user()
    elif choice == "3":
        afficher_user_ville(ville)
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_admin()

def menu_utilisateur():
    print("--- Menu Utilisateur ---")
    print("1. Afficher mes informations")
    print("2. Quitter")
    choice = input("Entrez votre choix: ")
    if choice == "1":
        afficher_user()
    elif choice == "2":
        print("Au revoir")
    else:
        print("Choix invalide")
        menu_utilisateur()