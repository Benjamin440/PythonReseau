import ConnectToDb as ConnectToDb
from User import User
from User import PHospitalier
from User import Patient

connect = ConnectToDb.connectdb()

EXE_OK = "L'exécution a été effectuée "

def countmatricule():
    cursor = connect[0]
    sql = """SELECT mat_user FROM utilisateur ORDER BY mat_user DESC limit 1"""
    cursor.execute(sql)
    res = cursor.fetchall()
    print("l'execution a été effectué")
    return res[0][0]

def insert_user(user=User):
    cursor = connect[0]
    sql = """
    INSERT INTO utilisateur (mat_user, nom, prenom, ville, numero, email, login, password, role, passwordv) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (user.get_mat_user(), user.get_nom(), user.get_prenom(), user.get_ville(), user.get_numero(), user.get_email(), user.get_login(), user.get_password(), user.get_role(), user.get_password_clear()))
    print(EXE_OK)
    connect[1].commit()

def insert_user_ph(user=PHospitalier):
    cursor = connect[0]
    sql = """
    INSERT INTO utilisateur (mat_user, nom, prenom, ville, numero, email, login, password, role, service, passwordv) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (user.get_mat_user(), user.get_nom(), user.get_prenom(), user.get_ville(), user.get_numero(), user.get_email(), user.get_login(), user.get_password(), user.get_role(), user.get_service(), user.get_password_clear()))
    print(EXE_OK)
    connect[1].commit()

def insert_user_patient(user=Patient):
    cursor = connect[0]
    sql = """
    INSERT INTO utilisateur (mat_user, nom, prenom, ville, numero, email, login, password, role, s_social, passwordv) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (user.get_mat_user(), user.get_nom(), user.get_prenom(), user.get_ville(), user.get_numero(), user.get_email(), user.get_login(), user.get_password(), user.get_role(), user.get_s_social(), user.get_password_clear()))
    print(EXE_OK)
    connect[1].commit()

def update_user(mat_user, column, value):
    cursor = connect[0]
    sql = f"UPDATE utilisateur SET {column} = %s WHERE mat_user = %s"
    try:
        cursor.execute(sql, (value, mat_user))
        connect[1].commit()
        print(EXE_OK)
    except Exception as e:
        connect[1].rollback()
        print(f"Erreur lors de la mise à jour : {e}")

def delete_user(matricule):
    cursor = connect[0]
    sql = f"DELETE FROM utilisateur  WHERE mat_user ={matricule};"
    cursor.execute(sql)
    print(EXE_OK)
    connect[1].commit()

def select_user(login):
    cursor = connect[0]
    sql = """SELECT * FROM utilisateur WHERE login = %s"""
    cursor.execute(sql, (login,))
    res = cursor.fetchall()
    return res

def select_user2(login):
    cursor = connect[0]
    sql = """SELECT nom,prenom,ville,numero,email,role,s_social,service FROM utilisateur WHERE login = %s"""
    cursor.execute(sql, (login,))
    res = cursor.fetchall()
    return res

def select_ville(ville):
    cursor = connect[0]
    sql = """SELECT nom,prenom,ville,numero,email,role FROM utilisateur WHERE ville = %s"""
    cursor.execute(sql, (ville,))
    res = cursor.fetchall()
    return res

def select_service(service):
    cursor = connect[0]
    sql = """SELECT nom,prenom,ville FROM utilisateur WHERE service = %s"""
    cursor.execute(sql, (service,))
    res = cursor.fetchall()
    return res


def close():
    connect[0].close()