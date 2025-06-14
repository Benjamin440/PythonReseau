FTP_HOST = "127.0.0.1"
FTP_PORT = 21
FTP_USER = input("Entrez le nom d'utilisateur FTP : ")
FTP_PASS = input("Entrez le mot de passe FTP : ")

REGIONS = ["Paris", "Marseille", "Rennes", "Grenoble"]
ROOT_DIR = "C:/New_Tech/Rennes"
FTP_DIRS = {
    "Paris": f"{ROOT_DIR}/Paris",
    "Marseille": f"{ROOT_DIR}/Marseille",
    "Rennes": f"{ROOT_DIR}/Rennes",
    "Grenoble": f"{ROOT_DIR}/Grenoble"
}