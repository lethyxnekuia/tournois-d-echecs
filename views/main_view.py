class MainView:

    def display_title(self):
        print("___________  Gestion De Tournoi  ___________")
        print("___________    Menu Principal    ___________")
        print("")

    def menu_choice(self, menu):
        for menu_key, menu_value in menu.items():
            print(f"{menu_key} : {menu_value['label']}")
        entry = input("Choisir parmis les propositions :")
        while entry not in menu:
            print("option invalide")
            entry = input("Choisir parmis les propositions :")
        print("____________________________________________")
        print("")
        return menu[entry]

    def impossible_action(self, info):
        print("Action impossible")
        print(info)
        print("____________________________________________")
        print("")

    def quit(self):
        print("___________      Au Revoir       ___________")
        print("")
