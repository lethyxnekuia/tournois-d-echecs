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

    def player_serializer(player):
        return {
            "name": player.name,
            "first_name": player.first_name,
            "birthday": player.birthday,
            "ranking": player.ranking,
            "player_id": player.player_id,
        }

    def validate_date(date):
        try:
            if date != datetime.strptime(date, "%Y-%m-%d"):
                return True
        except ValueError:
            return False
