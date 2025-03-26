from mechanics import class_selection
from enteties_factory import create_players
def bootstrap():
    print("Приветствуем в нашей текстовой игре")
    print("1. Новая игра\n2. Продолжить игру\n3. Выйти")


def gameloop():
    # user input
    is_gaming = True

    while is_gaming:
        user_input = int(input(">>"))
        if user_input == 3:
            is_gaming = False
            continue
        if user_input == 1:
            player_name = input("Как вас зовут >>")

            player_class = class_selection()

            player = create_players(player_name,player_class)
        

def dispose():
    print("Пока!")




