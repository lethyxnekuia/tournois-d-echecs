# chess_tournament

Project to manage Chess Tournament


## Creating Virtual environment, downloading and running the program:

```bash
git clone https://github.com/lethyxnekuia/tournois-d-echecs.git
cd tournois-d-echecs
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python main.py
```

## How to use chess_tournament?

### Menus

- for exemple the first menu is :
    1 : Menu Joueur
    2 : Menu Tournoi
    3 : Menu Sauvegarde
    4 : Quitter

-   write 1 to go to "Menu Joueur" 
-   write 2 to go to "Menu Tournoi"

### Save and Load Data

- In the "Menu Sauvegarde" you can save or load a data. the data is registred by default in data.json. 


## Flake8 and flake8-html report

### Generate an HTML report:

Open a terminal in chess_tournament folder and make sure virtual environment is activated.

flake8
```

Report will be generated in flake8 folder.