class Round(object):
    def __init__(self,
                 player_one=[],
                 player_two=[],
                 date_begin=None,
                 date_end=None,
                 round_id=0):
        self.player_one = player_one
        self.player_two = player_two
        self.date_begin = date_begin
        self.date_end = date_end
        self.round_id = round_id