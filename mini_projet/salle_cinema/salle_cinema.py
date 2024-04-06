from database import Connexion

class SalleCinema:
    def __init__(self):
        self.reservations = []

    def reserver_place(self, nom, place):
        self.reservations.append((nom, place))

    def afficher_places_reservées(self):
        for nom, place in self.reservations:
            print(f"Nom: {nom}, Place: {place}")

class SalleCinemaDAO:
    @staticmethod
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

    @staticmethod
    def recuperer_reservations():
        try:
            connexion = Connexion(host="localhost", user="utilisateur", password="mot_de_passe", database="nom_de_la_base")
            connexion.connect()
            query = "SELECT * FROM reservations"
            cursor = connexion.connexion.cursor(dictionary=True)
            cursor.execute(query)
            reservations = [(row['nom'], row['place']) for row in cursor.fetchall()]
            cursor.close()
            connexion.disconnect()
            print("Réservations récupérées avec succès")
            return reservations
        except Exception as e:
            print(f"Erreur lors de la récupération des réservations : {e}")
            return []
