from views import main_view
from views import player_view, tournament_view
from controllers import player_controller, tournament_controller, save_and_load_controller

class HomeMenuController:

    def __init__(self):
        self.running = True
        self.player_menu_controller = player_controller.PlayerMenuController([])
        self.tournament_menu_controller = tournament_controller.TournamentMenuController([],self.player_menu_controller.players)
        self.save_and_load_menu_controller = save_and_load_controller.SaveAndLoadMenuController(self.player_menu_controller.players,self.tournament_menu_controller.tournaments)
        self.main_menu = {
            "1" : {"label" : "Menu Joueur", "action" : self.player_menu_controller.start}, 
            "2" : {"label" : "Menu Tournoi", "action" : self.tournament_menu_controller.start},
            "3" : {"label" : "Menu Sauvegarde", "action" : self.save_and_load_menu_controller.start},
            "3" : {"label" : "Quitter", "action" : self.stop }
        }
        self.main_view = main_view.MainView()



    def start(self): 
        self.main_view.display_title()
        while self.running:
            entry = self.main_view.menu_choice(self.main_menu)
            entry["action"]()
        

    def stop(self):
        self.view = main_view.MainView.quit(self)
        self.running = False

        

class TournamentMenuController:

    def __init__(self, tournament):
        self

    def start(self):
        self.view = tournament_view.display_tournament_menu_title(self)


class QuitApp:

    def __init__(self):
        print("___________      Au Revoir       ___________")