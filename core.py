from mechanics import *
from enteties_factory import *
from roomconfigs import *
import time
from color_configs import *
from journey_creator import *

def bootstrap():
    print(f"{SYSTEM_COLOR}System >> Приветствуем в нашей текстовой игре{DEFAULT_COLOR}")
    print("1. Новая игра\n2. Выйти")


def gameloop():
    # user input
    is_gaming = True

    while is_gaming:
        user_input = int(input(">>"))
        if user_input == 3:
            is_gaming = False
            continue

        if user_input == 1:
            user_input,stages_list,player = create_dungeon()
            

        if user_input == 1:
            is_gaming = False
            continue

        is_searching = True
        stage_counter = 0

        for stage in stages_list:#stage_list[[stage],[stage],[stage]]
            if is_gaming == True and stage_counter == 0:
                print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Открываем первый этаж...{DEFAULT_COLOR}")

            elif is_gaming == True and stage_counter > 0:
                print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Этаж пройден\n{DEFAULT_COLOR}")
                time.sleep(4)
                print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Открываем новый этаж...{DEFAULT_COLOR}")

            elif not is_searching:
                break 
            
            for room in stage:#stage[[]]
                print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Открываем комнату{DEFAULT_COLOR}")
                time.sleep(1)

                if room[0] == LOOTBOX:
                    print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Вы наткнулись на сундук{DEFAULT_COLOR}")
                    time.sleep(1)
                    player = open_loot_box(player,room[1])

                elif room[0] == BOSS:
                    print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Вы наткнулись на босса{DEFAULT_COLOR}")
                    time.sleep(1)
                    fight_status = fight_boss(player,room[1])

                    if fight_status == False:
                        is_gaming = False
                        is_searching = False
                        break

                elif room[0] == MELEE:
                    print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Вы наткнулись на монстра{DEFAULT_COLOR}")
                    time.sleep(1)
                    fight_status = fight_monster_melee(player,room[1])

                    if fight_status == False:
                        is_gaming = False
                        is_searching = False
                        break
                        
                elif room[0] == RANGE:
                    print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Вы наткнулись на монстра{DEFAULT_COLOR}")
                    time.sleep(1)
                    fight_status = fight_monster_ranged(player,room[1])

                    if fight_status == False:
                        is_gaming = False
                        is_searching = False
                        break

                time.sleep(2)
                print(f"{'-'*20}\n{SYSTEM_COLOR}System >> Комната пройдена{DEFAULT_COLOR}")

            time.sleep(0.5)
            stage_counter+=1

        is_gaming = False


def dispose():
    print(f"{SYSTEM_COLOR}System >> Пока!{DEFAULT_COLOR}")




