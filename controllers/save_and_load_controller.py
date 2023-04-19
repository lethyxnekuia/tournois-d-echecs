
from views import  main_view

class SaveAndLoadMenuController:

    def __init__(self, players, tournaments):
        self.tournaments = tournaments
        self.players = players
        self.main_view = main_view.MainView()

    def start(self):
        self.save_menu = {
            "1" : {"label" : "Sauvegarder les données", "action" : self.save},
            "2" : {"label" : "Charger des données", "action" : self.load},
        }
        entry = self.main_view.menu_choice(self.save_menu)
        entry["action"]()

    def save(self):
        players = []
        tournaments = []
        for player in self.players:
            players.append(self.player_serializer(player))
        for tournament in self.tournaments:
            tournaments.append(self.tournament_serializer(tournament))
        save_dict ={
            "players" : players,
            "tournaments":tournaments
        }
        





    def player_serializer(player):
        return {
            "name": player.name,
            "first_name": player.first_name,
            "birthday": player.birthday,
            "ranking": player.ranking,
            "player_id":player.player_id,
        }
    
    def tournament_serializer(self, tournament):
        return {
            "tournament_name": tournament.tournament_name,
            "place": tournament.place,
            "date": tournament.date,
            "number_of_rounds": tournament.number_of_rounds,
            "description":tournament.description,
            "tournament_id":tournament.tournament_id,
            "players_by_ids": self.get_players_id(tournament.players),
            "rounds":self.get_rounds(tournament.rounds),
        }
    
    def get_players_id(self, players):
        players_id = []
        for player in players:
            players_id.append(player.player_id)
        return players_id
    
    def get_rounds(self, rounds):
        rounds = []
        for round in rounds:
            rounds.append(self.round_serializer(round))


    def round_serializer(self, round):
        return{
            "round_name":round.round_name,
            "date_begin":round.date_begin,
            "date_end":round.date_end,
            "match_list":self.get_match_list(round.match_list)
        }
    
    def get_match_list(self, match_list):
        return{
           "player_one":match_list[0][0].player_id,
           "score_player_one":match_list[0][1],
           "player_two":match_list[1][0].player_id,
           "score_player_two":match_list[1][1]   
        }