class PlayerView : 
    def display_player_menu_title(self):
        print("_____________    Menu Joueur    _____________")
        print("")

    def input_player(self):
        print("___________   Ajouter un joueur   ___________")
        print("")
        self.name = input("Nom : ")
        self.first_name = input("Prenom : ")
        self.birthday = input("Date de naissance (jj/mm/aaaa) : ")
        self.ranking = input("Veuillez saisir le numéro du classement : ")
        self.player_id = input("Veuillez saisir l'identifiant du joueur : ")
        print("____________________________________________")
        print("")
        return {
            "name": self.name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "ranking": self.ranking,
            "player_id": self.player_id,
            }
    
    def display_player(self, players) :
        print ("__________   Liste des Joueurs   __________")
        print("")
        for player in players :
            print(player.player_id, " : ", player.first_name, player.name)
        print("____________________________________________")
        print("")

    def display_select_a_player(self):
        print ("_______   Sélectionner un Joueur   ________")
        print("")