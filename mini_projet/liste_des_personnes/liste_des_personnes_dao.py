from database import Connexion

class ListePersonnesDAO:
    @staticmethod
    def sauvegarder_personne(personne):
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            query = f"INSERT INTO personnes (nom, age) VALUES ('{personne.nom}', {personne.age})"
            connexion.execute_query(query)
            connexion.disconnect()
            print("Personne sauvegardée avec succès")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la personne : {e}")

    @staticmethod
    def recuperer_personne(nom):
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            query = f"SELECT * FROM personnes WHERE nom = '{nom}'"
            cursor = connexion.connexion.cursor(dictionary=True)
            cursor.execute(query)
            personne_data = cursor.fetchone()
            cursor.close()
            connexion.disconnect()
            
            if personne_data:
                print("Personne récupérée avec succès")
                return Personne(personne_data['nom'], personne_data['age'])
            else:
                print("Personne non trouvée")
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération de la personne : {e}")
            return None
