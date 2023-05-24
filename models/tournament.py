from models.round import Round


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

    def tournament_serializer(self, tournament):
        return {
            "tournament_name": tournament.tournament_name,
            "place": tournament.place,
            "date": tournament.date,
            "number_of_rounds": tournament.number_of_rounds,
            "description": tournament.description,
            "tournament_id": tournament.tournament_id,
            "players": self.get_players_id(tournament.players),
            "rounds": self.get_rounds(tournament.rounds),
        }

    def get_players_id(self, players):
        players_id = []
        for player in players:
            players_id.append(player.player_id)
        return players_id

    def get_rounds(self, rounds):
        rounds = []
        for round in rounds:
            rounds.append(Round.round_serializer(round))
        return rounds
