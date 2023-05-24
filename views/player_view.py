import re
from models.player import Player
name_regex = re.compile('^[A-Z][A-Za-zéèêëïî-]+$')
id_regex = re.compile('^[a-zA-Z0-9]+$')
date_regex = re.compile('^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$')


class PlayerView:
    def display_player_menu_title(self):
        print("_____________    Menu Joueur    _____________")
        print("")

    def input_player(self):
        print("___________   Ajouter un joueur   ___________")
        print("")
        self.name = input("Nom : ")
        while name_regex.match(str(self.name)) is None:
            print("Veuillez rentrer un nom valide")
            self.name = input("Nom : ")
        self.first_name = input("Prenom : ")
        while name_regex.match(str(self.first_name)) is None:
            print("Veuillez rentrer un prénom valide")
            self.first_name = input("Prenom : ")
        self.birthday = input("Date de naissance (aaaa-mm-jj) : ")
        while not Player.validate_date(self.birthday):
            print("Veuillez rentrer une date valide")
            self.birthday = input("Date du tournoi (aaaa-mm-jj) : ")
        self.ranking = input("Veuillez saisir le numéro du classement : ")
        while not self.ranking.isdigit():
            print("Veuillez rentrer un numéro valide")
            self.ranking = input("Veuillez saisir le numéro du classement : ")
        self.player_id = input("Veuillez saisir l'identifiant du joueur : ")
        while id_regex.match(str(self.player_id)) is None:
            print("Veuillez rentrer un identifiant valide")
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

    def display_player(self, players):
        print("__________   Liste des Joueurs   __________")
        print("")
        for player in players:
            print(player.player_id, " : ", player.first_name, player.name)
        print("____________________________________________")
        print("")

    def display_select_a_player(self):
        print("_______   Sélectionner un Joueur   ________")
        print("")
