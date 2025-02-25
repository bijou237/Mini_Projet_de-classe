from database import Connexion

class FileAttente:
    def __init__(self):
        self.attente = []

    def ajouter_personne_en_attente(self, nom):
        self.attente.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente:
            return self.attente.pop(0)
        else:
            return None

class FileAttenteDAO:
    @staticmethod
    def sauvegarder_attente(attente):
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            for personne in attente.attente:
                query = f"INSERT INTO file_attente (nom) VALUES ('{personne}')"
                connexion.execute_query(query)
            connexion.disconnect()
            print("File d'attente sauvegardée avec succès")
        except Exception as error:
            print(f"Erreur lors de la sauvegarde de la file d'attente : {e}")

    @staticmethod
    def recuperer_attente():
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            query = "SELECT * FROM file_attente"
            cursor = connexion.connexion.cursor(dictionary=True)
            cursor.execute(query)
            attente = [row['nom'] for row in cursor.fetchall()]
            cursor.close()
            connexion.disconnect()
            print("File d'attente récupérée avec succès")
            return attente
        except Exception as error:
            print(f"Erreur lors de la récupération de la file d'attente : {e}")
            return []
