
from views import player_view, main_view
from models.player import Player


class PlayerMenuController:

    def __init__(self, players):
        self.players = players
        self.view = player_view.PlayerView()
        self.main_view = main_view.MainView()

    def start(self):
        self.player_menu = {
            "1": {"label": "Créer un Joueur", "action": self.create_player},
            "2": {"label": "Liste des Joueurs", "action": self.player_list},
        }
        entry = self.main_view.menu_choice(self.player_menu)
        entry["action"]()

    def create_player(self):
        player = self.view.input_player()
        new_player = Player(
            player["name"],
            player["first_name"],
            player["birthday"],
            player["ranking"],
            player["player_id"]
        )
        self.players.append(new_player)

    def player_list(self):
        players = sorted(self.players, key=lambda player: player.name)
        self.view.display_player(players)
