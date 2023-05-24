
import json
from views import main_view
from models.player import Player
from models.tournament import Tournament
from models.round import Round


class SaveAndLoadMenuController:

    def __init__(self, players, tournaments):
        self.tournaments = tournaments
        self.players = players
        self.main_view = main_view.MainView()

    def start(self):
        self.save_menu = {
            "1": {"label": "Sauvegarder les données", "action": self.save},
            "2": {"label": "Charger des données", "action": self.load},
        }
        entry = self.main_view.menu_choice(self.save_menu)
        entry["action"]()

    def save(self):
        players = []
        tournaments = []
        for player in self.players:
            players.append(Player.player_serializer(player))
        for tournament in self.tournaments:
            tournaments.append(Tournament.tournament_serializer(tournament))
        save_dict = {
            "players": players,
            "tournaments": tournaments
        }
        with open("data.json", "w") as outfile:
            json.dump(save_dict, outfile)

    def load(self):
        with open('data.json') as data:
            data = json.load(data)
        for player in data["players"]:
            new_player = Player(
                player["name"],
                player["first_name"],
                player["birthday"],
                player["ranking"],
                player["player_id"]
            )
            self.players.append(new_player)
        for tournament in data["tournaments"]:
            new_tournament = Tournament(
                tournament["tournament_name"],
                tournament["place"],
                tournament["date"],
                int(tournament["number_of_rounds"]),
                tournament["description"],
                tournament["tournament_id"],
                self.load_players(tournament["players"]),
                self.load_rounds(tournament["rounds"])
            )
            self.tournaments.append(new_tournament)

    def load_players(self, players_id):
        players = []
        for player_id in players_id:
            player = self.load_player(player_id)
            players.append(player)
        return players

    def load_player(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player

    def load_rounds(self, rounds_data):
        rounds = []
        for round_data in rounds_data:
            round = Round(
                round_data["round_name"],
                round_data["date_begin"],
                round_data["date_end"],
                self.load_matchs(round_data["mactch_list"])
            )
            rounds.append(round)
        return rounds

    def load_matchs(self, matchs_data):
        matchs = []
        for match_data in matchs_data:
            match = [
                (self.load_player(match_data["player_one"][0]), match_data["player_one"][1]),
                (self.load_player(match_data["player_two"][0]), match_data["player_two"][1])
            ]
            matchs.append(match)
        return matchs
