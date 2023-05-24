class Round(object):
    def __init__(self,
                 round_name,
                 date_begin,
                 date_end,
                 mactch_list=None,
                 ):
        self.round_name = round_name
        self.date_begin = date_begin
        self.date_end = date_end
        self.mactch_list = mactch_list if mactch_list is not None else []

    def round_serializer(self, round):
        return {
            "round_name": round.round_name,
            "date_begin": round.date_begin,
            "date_end": round.date_end,
            "match_list": self.get_match_list(round.match_list)
        }

    def get_match_list(self, match_list):
        return {
           "player_one": [match_list[0][0].player_id, match_list[0][1]],
           "player_two": [match_list[1][0].player_id, match_list[1][1]]
        }
