
from views import tournament_view, main_view, player_view
from models.tournament import Tournament
from models.round import Round
import random
from datetime import datetime


class TournamentMenuController:

    def __init__(self, tournaments, players):
        self.tournaments = tournaments
        self.players = players
        self.view = tournament_view.TournamentView()
        self.main_view = main_view.MainView()
        self.player_view = player_view.PlayerView()

    def start(self):
        self.tournament_menu = {
            "1": {"label": "Créer un Tournoi", "action": self.create_tournament},
            "2": {"label": "Liste des Tournois", "action": self.tournament_list},
            "3": {"label": "Ajouter un joueur à un Tournoi", "action": self.add_player_to_tournament},
            "4": {"label": "Lancer un Round", "action": self.create_a_round},
            "5": {"label": "Remplir les scores d'un Round", "action": self.write_score},
            "6": {"label": "Liste des joueurs d'un Tournoi", "action": self.tournament_players},
            "7": {"label": "Nom et Date d'un Tournoi", "action": self.tournament_date_and_name},
            "8": {"label": "Liste des rounds d'un Tournoi", "action": self.tournament_rounds},
            "9": {"label": "Liste des matchs d'un Round", "action": self.tournament_round_matchs},
        }
        entry = self.main_view.menu_choice(self.tournament_menu)
        entry["action"]()

    def create_tournament(self):
        tournament = self.view.input_tournament()
        new_tournament = Tournament(
            tournament["tournament_name"],
            tournament["place"],
            tournament["date"],
            int(tournament["number_of_rounds"]),
            tournament["description"],
            tournament["tournament_id"],
        )
        self.tournaments.append(new_tournament)

    def tournament_list(self):
        self.view.display_tournament(self.tournaments)

    def add_player_to_tournament(self):
        self.player_view.display_select_a_player()
        self.player_choice_menu = {}
        self.tounament_choice_menu = {}

        if not self.tournaments:
            self.main_view.impossible_action()
            return

        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        if tournament.rounds.length > 0:
            self.main_view.impossible_action()
            return
        filtered_players_list = self.players_list_filter(self.players, tournament.players)
        if not filtered_players_list:
            self.main_view.impossible_action()
            return

        for count, player in enumerate(filtered_players_list, start=1):
            self.player_choice_menu[f"{count}"] = {"label": player.player_id, "player": player}

        player = self.main_view.menu_choice(self.player_choice_menu)
        tournament.players.append(player["player"])

    def players_list_filter(self, players, tournament_players):
        filtered_players = []
        for player in players:
            test = True
            for tournament_player in tournament_players:
                if tournament_player == player:
                    test = False
            if test:
                filtered_players.append(player)
        return filtered_players

    def tournament_choice(self, tournaments):
        self.tounament_choice_menu = {}
        for count, tournament in enumerate(tournaments, start=1):
            self.tounament_choice_menu[f"{count}"] = {
                "label": tournament.tournament_name,
                "id": tournament.tournament_id
                }
        tournament_index = self.view.tournament_choice(self.tounament_choice_menu)
        return tournament_index

    def create_a_round(self):
        self.tounament_choice_menu = {}
        if not self.tournaments:
            self.main_view.impossible_action()
            return

        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        if len(tournament.rounds) > 0 and not tournament.rounds[-1].date_end:
            self.main_view.impossible_action()
            return

        players_list = tournament.players
        players_count = len(players_list)
        if players_count < 2 or players_count % 2 != 0 or len(tournament.rounds) >= tournament.number_of_rounds:
            self.main_view.impossible_action()
            return

        player_list_with_score = self.add_score_to_player(players_list, tournament)
        sorted_players = sorted(player_list_with_score, key=lambda player: player["tournament_score"])
        round_match_list = []
        for i in range(1, players_count//2):
            player_one = sorted_players[0]
            count = 1
            potential_choice_list = []
            while count != 0 or count >= len(sorted_players):
                potential_player = self.potential_player(
                    player_one["player"], sorted_players[count]["player"],
                    tournament.rounds
                )
                if not potential_player:
                    count = count + 1
                else:
                    potential_choice_list.append(sorted_players[count])
                    if self.isOverPotentialPlayer(count, sorted_players, sorted_players[count]["tournament_score"]):
                        count = count + 1
                    else:
                        player_two_index = random.randrange(len(potential_choice_list))
                        player_two = potential_choice_list[player_two_index]
                        round_match_list.append([(player_one["player"], 0), (player_two["player"], 0)])
                        sorted_players.remove(player_one)
                        sorted_players.remove(player_two)
                        count = 0
                count = 0
        while sorted_players != []:
            round_match_list.append([(sorted_players[0]["player"], 0), (sorted_players[1]["player"], 0)])
            sorted_players.remove(sorted_players[0])
            sorted_players.remove(sorted_players[1])
        round = self.create_round_instance(round_match_list, tournament)
        tournament.rounds.append(round)

    def isOverPotentialPlayer(self, count, sorted_players, tournament_score_one):
        if count < (len(sorted_players) - 1):
            tournament_score_two = sorted_players[count + 1]["tournament_score"]
            if tournament_score_one == tournament_score_two:
                return True
        return False

    def add_score_to_player(self, player_list, tournament):
        list_with_score = []
        for player in player_list:
            tournament_score = 0
            for round in tournament.rounds:
                for match in round.match_list:
                    if match[0][0] == player:
                        tournament_score += match[0][1]
                    if match[1][0] == player:
                        tournament_score += match[1][1]
            list_with_score.append({"player": player, "tournament_score": tournament_score})
        return list_with_score

    def create_round_instance(self, round_match_list, tournament):
        round_number = len(tournament.rounds)
        new_round = Round(
            "Round " + str(round_number + 1),
            datetime.now(),
            None,
            round_match_list,
        )
        print(new_round)
        return new_round

    def potential_player(self, player_one, player_two, rounds):
        for round in rounds:
            for match in round.match_list:
                if match[0][0] == player_one:
                    if match[1][0] == player_two:
                        return False
                elif match[1][0] == player_one:
                    if match[0][0] == player_two:
                        return False
        return True

    def write_score(self):
        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        if tournament.rounds[-1].date_end:
            self.main_view.impossible_action()
            return

        match_list_choice = {}
        for count, match in enumerate(tournament.rounds[-1].match_list, start=1):

            if match[0][1] == 0 and match[1][1] == 0:
                match_list_choice[f"{count}"] = {"player_one": match[0][0].name,  "player_two": match[1][0].name}

        match_index = int(self.view.match_choice(match_list_choice))-1
        match = tournament.rounds[-1].match_list[match_index]
        winner = int(self.view.select_winner(match))
        if winner == 1:
            match[0] = (match[0][0], 1)
        if winner == 2:
            match[1] = (match[1][0], 1)
        if winner == 3:
            match[0] = (match[0][0], 0.5)
            match[1] = (match[1][0], 0.5)

        if len(match_list_choice) == 1:
            tournament.rounds[-1].date_end = datetime.now()

    def tournament_players(self):
        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        players = sorted(tournament.players, key=lambda player: player.name)
        self.player_view.display_player(players)

    def tournament_date_and_name(self):
        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        self.view.tournament_date_and_name(tournament)

    def tournament_rounds(self):
        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        self.view.tournament_rounds(tournament)

    def tournament_round_matchs(self):
        tournament_index = int(self.tournament_choice(self.tournaments)) - 1
        tournament = self.tournaments[tournament_index]
        rounds = []
        for count, round in enumerate(tournament.rounds, start=1):
            rounds[f"{count}"] = {"Nom": round.round_name}
        round_index = int(self.main_view.menu_choice(rounds)) - 1
        round = tournament.rounds[round_index]
        self.view.tournament_round_matchs(tournament)
