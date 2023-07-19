
import json
from views import main_view
from models.player import Player
from models.tournament import Tournament


class SaveAndLoadMenuController:

    def __init__(self, players, tournaments):
        self.tournaments = tournaments
        self.players = players
        self.main_view = main_view.MainView()

    def start(self):
        self.save_menu = {
            "1": {"label": "Sauvegarder les données", "action": self.save},
            "2": {"label": "Charger des données", "action": self.load},
            "3": {"label": "Retour", "action": self.back},
        }
        entry = self.main_view.menu_choice(self.save_menu)
        entry["action"]()

    def back(self):
        return

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
        self.players.clear()
        self.tournaments.clear()
        try:
            with open('data.json') as data:
                data = json.load(data)
            for player in data["players"]:
                new_player = Player.player_loader(player)
                self.players.append(new_player)
            for tournament in data["tournaments"]:
                new_tournament = Tournament.tournament_loader(tournament, self.players)
                self.tournaments.append(new_tournament)
        except:
            self.main_view.impossible_action()
            return

