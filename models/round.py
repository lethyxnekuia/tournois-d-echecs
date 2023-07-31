from models.player import Player
from datetime import datetime


class Round(object):
    def __init__(self,
                 round_name,
                 date_begin,
                 date_end,
                 match_list=None,
                 ):
        self.round_name = round_name
        self.date_begin = date_begin
        self.date_end = date_end
        self.match_list = match_list if match_list is not None else []

    @staticmethod
    def round_serializer(round):
        date_end = None
        if round.date_end:
            date_end = round.date_end.strftime("%Y-%m-%d")
        return {
            "round_name": round.round_name,
            "date_begin": round.date_begin.strftime("%Y-%m-%d"),
            "date_end": date_end,
            "match_list": Round.get_match_list(round.match_list)
        }

    @staticmethod
    def get_match_list(match_list):
        matchs = []
        for match in match_list:
            matchs.append({
                "player_one": [match[0][0].player_id, match[0][1]],
                "player_two": [match[1][0].player_id, match[1][1]]
            })
        return matchs

    @staticmethod
    def load_rounds(rounds_data, players):
        rounds = []
        for round_data in rounds_data:
            if round_data["date_end"]:
                round_data["date_end"] = datetime.strptime(round_data["date_end"], "%Y-%m-%d")
            rounds.append(Round(
                round_data["round_name"],
                datetime.strptime(round_data["date_begin"], "%Y-%m-%d"),
                round_data["date_end"],
                Round.load_matchs(round_data["match_list"], players)
            ))
        return rounds

    @staticmethod
    def load_matchs(matchs_data, players):
        matchs = []
        for match_data in matchs_data:
            match = [
                (Player.load_player(match_data["player_one"][0], players), match_data["player_one"][1]),
                (Player.load_player(match_data["player_two"][0], players), match_data["player_two"][1])
            ]
            matchs.append(match)
        return matchs
