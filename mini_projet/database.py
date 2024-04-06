import mysql.connector as mysql

class Connexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = "ecole"
        self.connexion = None

    def connect(self):
        try:
            self.connexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connexion à la base de données réussie")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")

    def disconnect(self):
        if self.connexion:
            self.connexion.close()
            print("Déconnexion de la base de données")

    def execute_query(self, query):
        try:
            cursor = self.connexion.cursor()
            cursor.execute(query)
            self.connexion.commit()
            print("Requête exécutée avec succès")
            cursor.close()
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")

# Utilisation de la classe Connexion pour se connecter à la base de données
connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
connexion.connect()

# Exemple d'exécution d'une requête SQL
query = "SELECT * FROM table"
connexion.execute_query(query)

# Déconnexion de la base de données
connexion.disconnect()
