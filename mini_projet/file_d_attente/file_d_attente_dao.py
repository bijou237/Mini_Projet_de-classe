from database import Connexion

class FileAttenteDAO:
    @staticmethod
    def sauvegarder_attente(attente):
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            for personne in attente:
                query = f"INSERT INTO file_attente (nom) VALUES ('{personne}')"
                connexion.execute_query(query)
            connexion.disconnect()
            print("File d'attente sauvegardée avec succès")
        except Exception as e:
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
        except Exception as e:
            print(f"Erreur lors de la récupération de la file d'attente : {e}")
            return []
