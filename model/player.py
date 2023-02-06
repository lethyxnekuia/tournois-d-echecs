class Player(object):
    def __init__(self,
                 name=None,
                 first_name=None,
                 birthday=None,
                 ranking=None,
                 tournament_score=0,
                 player_id=0):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.ranking = ranking
        self.tournament_score = tournament_score
        self.player_id = player_id