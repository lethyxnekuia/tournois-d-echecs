import re
from models.player import Player
name_regex = re.compile('^[A-Z][A-Za-zéèêëïî-]+$')
id_regex = re.compile('^[a-zA-Z0-9]+$')


class TournamentView:
    def display_tournament_menu_title(self):
        print("____________    Menu Tournoi    ____________")
        print("")

    def input_tournament(self):
        print("__________   Ajouter un Tournoi  ___________")
        print("")
        self.tournament_name = input("Nom du tournoi: ")
        while name_regex.match(str(self.tournament_name)) is None:
            print("Veuillez rentrer un nom valide")
            self.tournament_name = input("Nom : ")
        self.place = input("lieu du tournoi : ")
        while name_regex.match(str(self.place)) is None:
            print("Veuillez rentrer un lieu valide")
            self.place = input("lieu du tournoi : ")
        self.date = Player.validate_date(input("Date du tournoi (aaaa-mm-jj) : "))
        while not self.date:
            print("Veuillez rentrer une date valide")
            self.date = Player.validate_date(input("Date du tournoi (aaaa-mm-jj) : "))
        self.number_of_rounds = input("Nombre de rounds : ")
        while not self.number_of_rounds.isdigit() and self.number_of_rounds != "0":
            print("Veuillez rentrer un nombre valide")
            self.number_of_rounds = input("Nombre de rounds : ")
        self.description = input("Description du tournoi : ")
        self.tournament_id = input("Identifiant du tournoi : ")
        while id_regex.match(str(self.tournament_id)) is None:
            print("Veuillez rentrer un id valide")
            self.tournament_id = input("Identifiant du tournoi : ")
        print("____________________________________________")
        print("")
        return {
            "tournament_name": self.tournament_name,
            "place": self.place,
            "date": self.date,
            "number_of_rounds": self.number_of_rounds,
            "description": self.description,
            "tournament_id": self.tournament_id
            }

    def display_tournament(self, tournaments):
        print("__________   Liste des Tournois   _________")
        print("")
        for tournament in tournaments:
            print(tournament.tournament_id, " : ", tournament.tournament_name, ", ", tournament.place)
        print("____________________________________________")
        print("")

    def tournament_choice(self, menu):
        print("_______   Sélectionner un Tournoi   _______")
        print("")
        for menu_key, menu_value in menu.items():
            print(f"{menu_key} : {menu_value['label']}")
        entry = input("Choisir parmis les propositions :")
        while entry not in menu:
            print("option invalide")
            entry = input("Choisir parmis les propositions :")
        print("____________________________________________")
        print("")
        return entry

    def match_choice(self, menu):
        print("________   Sélectionner un Match   ________")
        print("")
        for menu_key, menu_value in menu.items():
            print(f"{menu_key} : {menu_value['player_one']} vs {menu_value['player_two']}")
        entry = input("Choisir parmis les propositions :")
        while entry not in menu:
            print("option invalide")
            entry = input("Choisir parmis les propositions :")
        print("____________________________________________")
        print("")
        return entry

    def select_winner(self, match):
        print("________   Sélectionner un Vainqueur   ________")
        print(f"1 : {match[0][0].name}")
        print(f"2 : {match[1][0].name}")
        print("3 : Match Nul")
        entry = input("Choisir parmis les propositions :")
        while entry not in ["1", "2", "3"]:
            print("option invalide")
            entry = input("Choisir parmis les propositions :")
        print("____________________________________________")
        print("")
        return entry

    def tournament_date_and_name(self, tournament):
        print(f"Nom: {tournament.tournament_name}")
        print(f"Date: {tournament.date}")

    def tournament_rounds(self, tournament):
        for round in tournament.rounds:
            print(f"Nom: {round.round_name}, Date de début: {round.date_begin}, Date de fin: {round.date_end}")

    def tournament_round_matchs(self, round):
        for match in round.match_list:
            print(f"Joueur 1: {match[0][0].name}, Score:  {match[0][1]}")
            print(f"Joueur 2: {match[1][0].name}, Score:  {match[1][1]}")
