class Tournament(object):
    def __init__(self,
                 tournament_name=None,
                 place=None,
                 date=None,
                 rounds=4,
                 description=None,
                 list_id_players=None,
                 list_of_rounds=[],
                 tournament_id=None):
        self.tournament_name = tournament_name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.description = description
        self.list_id_players = list_id_players
        self.list_of_rounds = list_of_rounds
        self.tournament_id = tournament_id