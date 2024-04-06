# Import des classes nécessaires
from salle_cinema.salle_cinema import SalleCinema

# Création d'une instance de SalleCinema
salle_cinema = SalleCinema()

# Appel de la méthode reserver_place pour réserver une place dans la salle de cinéma
salle_cinema.reserver_place("John", 5)

# Appel de la méthode afficher_places_reservées pour afficher les places réservées
print("Places réservées :")
salle_cinema.afficher_places_reservées()

# Appel de la méthode nombre_places_disponibles pour afficher le nombre de places disponibles
print("Nombre de places disponibles :", salle_cinema.nombre_places_disponibles())

# Appel de la méthode filtrer_reservations_par_personne pour filtrer les réservations par personne
print("Réservations pour John :")
salle_cinema.filtrer_reservations_par_personne("John")

# Appel de la méthode annuler_reservation pour annuler les réservations pour une personne
salle_cinema.annuler_reservation("John")

# Appel de la méthode reserver_place_speciale pour réserver une place spéciale
salle_cinema.reserver_place_speciale("Alice")
