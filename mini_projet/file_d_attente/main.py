# Import des classes nécessaires
from file_d_attente.file_d_attente_dao import FileAttenteDAO
from file_d_attente.file_d_attente import FileAttente

# Création d'une instance de FileAttente
file_attente = FileAttente()

# Appel de la méthode ajouter_personne_en_attente pour ajouter une personne à la file d'attente
file_attente.ajouter_personne_en_attente("John")

# Appel de la méthode supprimer_personne_de_attente pour supprimer la première personne de la file d'attente
personne_supprimee = file_attente.supprimer_personne_de_attente()

# Affichage de la personne supprimée, s'il y en a une
if personne_supprimee:
    print(f"La personne {personne_supprimee} a été supprimée de la file d'attente.")
else:
    print("La file d'attente est vide.")
