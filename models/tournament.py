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

    


