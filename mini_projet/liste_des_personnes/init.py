# Import des classes nécessaires
from liste_des_personnes.liste_des_personnes_dao import ListePersonnesDAO
from liste_des_personnes.liste_des_personnes import Personne

# Création d'une instance de Personne
nouvelle_personne = Personne("John Doe", 30)

# Appel de la méthode sauvegarder_personne de ListePersonnesDAO pour sauvegarder la personne
ListePersonnesDAO.sauvegarder_personne(nouvelle_personne)

# Appel de la méthode recuperer_personne de ListePersonnesDAO pour récupérer une personne par son nom
personne_recuperee = ListePersonnesDAO.recuperer_personne("John Doe")

# Affichage des détails de la personne récupérée, s'il y en a une
if personne_recuperee:
    print(f"Nom: {personne_recuperee.nom}, Age: {personne_recuperee.age}")
else:
    print("Personne non trouvée dans la base de données.")
