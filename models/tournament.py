from models.round import Round
from models.player import Player
from datetime import datetime


class Tournament(object):
    def __init__(self,
                 tournament_name,
                 place,
                 date,
                 number_of_rounds,
                 description,
                 tournament_id,
                 players=None,
                 rounds=None):
        self.tournament_name = tournament_name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.tournament_id = tournament_id
        self.players = players if players is not None else []
        self.rounds = rounds if rounds is not None else []

    @staticmethod
    def tournament_serializer(tournament):
        return {
            "tournament_name": tournament.tournament_name,
            "place": tournament.place,
            "date": tournament.date.strftime("%Y-%m-%d"),
            "number_of_rounds": tournament.number_of_rounds,
            "description": tournament.description,
            "tournament_id": tournament.tournament_id,
            "players": Tournament.get_players_id(tournament.players),
            "rounds": Tournament.get_rounds(tournament.rounds),
        }

    @staticmethod
    def get_players_id(players):
        players_id = []
        for player in players:
            players_id.append(player.player_id)
        return players_id

    @staticmethod
    def get_rounds(rounds):
        rounds_list = []
        for round in rounds:
            rounds_list.append(Round.round_serializer(round))
        return rounds_list

    @staticmethod
    def tournament_loader(tournament, players):
        return Tournament(
            tournament["tournament_name"],
            tournament["place"],
            datetime.strptime(tournament["date"], "%Y-%m-%d"),
            int(tournament["number_of_rounds"]),
            tournament["description"],
            tournament["tournament_id"],
            Player.load_players(tournament["players"], players),
            Round.load_rounds(tournament["rounds"], players)
            )

    @staticmethod
    def unique_id(tournaments, id):
        for tournament in tournaments:
            if tournament.tournament_id == id:
                return False
        return True
