from mechanics import *
from enteties_factory import create_players
from enteties_factory import create_stage
from roomconfigs import *
import time
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
            stages = 5
            stages_list = []
        for i in range(0,stages,1):
            stages_list.append(create_stage(player))
        print("Хотите ли вы начать свое приключение?(1-нет;2-да)")
        user_input = int(input())
        if user_input == 1:
            is_gaming = False
            continue
        is_searching = True
        stage_counter = 0
        for stage in stages_list:#stage_list[[stage],[stage],[stage]]
            if is_gaming == True and stage_counter == 0:
                print(f"{'-'*20}\nоткрываем первый этаж...\n{'-'*20}")

            if is_gaming == True and stage_counter > 0:
                print(f"{'-'*20}\nЭтаж пройден\n{'-'*20}")
                time.sleep(4)
                print(f"{'-'*20}\nоткрываем новый этаж...\n{'-'*20}")

            if not is_searching:
                break 
            
            for room in stage:#stage[[]]
                if room[0] == LOOTBOX:
                    open_loot_box(player,room[1])

                if room[0] == BOSS:
                    fight_boss(player,room[1])

                if room[0] == MELEE:
                    fight_status = fight_monster_melee(player,room[1])
                    if fight_status == False:
                        is_gaming = False
                        is_searching = False
                        break
                        
                if room[0] == RANGE:
                    fight_status = fight_monster_ranged(player,room[1])
                    if fight_status == False:
                        is_gaming = False
                        is_searching = False
                        break

                time.sleep(2)
                print(f"{'-'*20}\nКомната пройдена\n{'-'*20}")
            time.sleep(2)
            stage_counter+=1
        
        

def dispose():
    print("Пока!")




