from datetime import datetime


class Player(object):
    def __init__(self,
                 name,
                 first_name,
                 birthday,
                 ranking,
                 player_id=0):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.ranking = ranking
        self.player_id = player_id

    @staticmethod
    def player_serializer(player):
        return {
            "name": player.name,
            "first_name": player.first_name,
            "birthday": player.birthday.strftime("%Y-%m-%d"),
            "ranking": player.ranking,
            "player_id": player.player_id,
        }

    @staticmethod
    def player_loader(player):
        return Player(
                player["name"],
                player["first_name"],
                datetime.strptime(player["birthday"], "%Y-%m-%d"),
                player["ranking"],
                player["player_id"]
            )

    @staticmethod
    def validate_date(date):
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False

    @staticmethod
    def validate_birth_date(date):
        try:
            formated_date = datetime.strptime(date, "%Y-%m-%d")
            if datetime.now() < formated_date:
                return False
            return formated_date
        except ValueError:
            return False

    @staticmethod
    def load_players(players_id, players):
        tournament_players = []
        for player_id in players_id:
            player = Player.load_player(player_id, players)
            tournament_players.append(player)
        return tournament_players

    @staticmethod
    def load_player(player_id, players):
        for player in players:
            if player.player_id == player_id:
                return player

    @staticmethod
    def unique_id(players, id):
        for player in players:
            if player.player_id == id:
                return False
        return True
