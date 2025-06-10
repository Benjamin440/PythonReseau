import psycopg2

def connectdb():
    db_conection = psycopg2.connect(database="projet_python", user='postgres', password='|)r6>|}ST87B', host="82.67.90.50", port=5432)
    try:
        cursor = db_conection.cursor()
        print("Connection à la base de donnée réussie")
    except psycopg2.Error:
        raise ValueError("La connection à la base de donnée n'as pas fonctionnée")
    return (cursor,db_conection)
    