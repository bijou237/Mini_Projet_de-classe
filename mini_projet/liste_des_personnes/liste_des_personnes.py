import mysql.connector as mysql

class ListePersonnesDAO:
    @classmethod
    def sauvegarder_personne(personne):
        # Connexion à la base de données MySQL
        connexion = mysql.connector.connect(
            host="localhost",
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            database="votre_base_de_donnees"
        )

        # Requête SQL pour insérer une personne dans la table "Personnes"
        query = "INSERT INTO Personnes (nom, age) VALUES (%s, %s)"
        values = (personne.nom, personne.age)

        try:
            # Création du curseur
            cursor = connexion.cursor()

            # Exécution de la requête SQL
            cursor.execute(query, values)

            # Validation de la transaction
            connexion.commit()

            print("Personne sauvegardée avec succès dans la base de données.")
        except mysql.connector.Error as e:
            # En cas d'erreur, annuler la transaction
            connexion.rollback()
            print(f"Erreur lors de la sauvegarde de la personne : {e}")
        finally:
            # Fermeture du curseur et de la connexion à la base de données
            if 'cursor' in locals():
                cursor.close()
            connexion.close()

    @classmethod
    def recuperer_personne(nom):
        # Connexion à la base de données MySQL
        connexion = mysql.connector.connect(
            host="localhost",
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            database="votre_base_de_donnees"
        )

        # Requête SQL pour récupérer une personne par son nom dans la table "Personnes"
        query = "SELECT * FROM Personnes WHERE nom = %s"
        values = (nom,)

        try:
            # Création du curseur
            cursor = connexion.cursor()

            # Exécution de la requête SQL
            cursor.execute(query, values)

            # Récupération du résultat de la requête
            personne = cursor.fetchone()

            if personne:
                print("Personne récupérée avec succès depuis la base de données.")
                return Personne(personne[0], personne[1])  # Création et renvoi d'un objet Personne
            else:
                print("Personne non trouvée dans la base de données.")
                return None
        except connexion as error:
            print(f"Erreur lors de la récupération de la personne : {e}")
            return None
        finally:
            # Fermeture du curseur et de la connexion à la base de données
            if 'cursor' in locals():
                cursor.close()
            connexion.close()
