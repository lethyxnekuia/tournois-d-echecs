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
