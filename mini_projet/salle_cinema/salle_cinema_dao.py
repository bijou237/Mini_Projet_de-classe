from database import Connexion

class SalleCinemaDAO:
    @classmethod
    def sauvegarder_reservation(nom, place):
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            query = f"INSERT INTO reservations (nom, place) VALUES ('{nom}', {place})"
            connexion.execute_query(query)
            connexion.disconnect()
            print("Réservation sauvegardée avec succès")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la réservation : {e}")

    @classmethod
    def recuperer_reservations():
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            query = "SELECT * FROM reservations"
            cursor = connexion.connexion.cursor(dictionary=True)
            cursor.execute(query)
            reservations = cursor.fetchall()
            cursor.close()
            connexion.disconnect()
            print("Réservations récupérées avec succès")
            return reservations
        except Exception as e:
            print(f"Erreur lors de la récupération des réservations : {e}")
            return []
