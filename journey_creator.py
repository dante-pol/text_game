from mechanics import *
from enteties_factory import *
from enteties_factory import __create_ranged_monster
from enteties_factory import __create_monster_melee
from roomconfigs import *
from color_configs import *
import tabulate


def class_selection():
   print("Выберите свой класс")
   classes = [
       ["выбор","название","урон","жизни","бонус урона","бонус жизней"],
       [0,"Maг",8,60,5,6],
       [1,"Рыцарь",5,80,3,8],
       [2,"Охотник",8,75,3,8],
       [3,"Aссасин",8,65,3,8],
       [4,"Паладин",3,90,4,6]
   ]
   output = tabulate.tabulate(classes)
   print(output)
   player_class = int(input(f"{SYSTEM_COLOR}System >> Ваш выбор:{DEFAULT_COLOR}"))

   return player_class

def create_dungeon():
    player_name = input(f"{SYSTEM_COLOR}System >>Как вас зовут:{DEFAULT_COLOR}")

    player_class = class_selection()

    player = create_player(player_name,player_class)
    stages = 5
    stages_list = []

    print(f"{SYSTEM_COLOR}System >> Хотите ли вы начать свое приключение?(1-нет;2-да):{DEFAULT_COLOR}")
    user_input = int(input())

    for i in range(0,stages,1):
        stages_list.append(create_stages())
    
    return user_input,stages_list,player


def create_stages():
    import random
    import roomconfigs as rc
    
    stage_index = random.randint(0,len(rc.stages)-1)
    config = rc.stages[stage_index]
    stage = []

    for room in config:
        if room == rc.MONSTER:
            id = random.randint(3,4)

            if id == 3:
              stage.append([rc.MELEE,__create_monster_melee()])

            elif id == 4:
                stage.append([rc.RANGE,__create_ranged_monster()])
            
    
        elif room == rc.LOOTBOX:
            stage.append([rc.LOOTBOX,create_loot_box()])

        elif room == rc.BOSS:
            stage.append([rc.BOSS,create_boss()])

    return stage