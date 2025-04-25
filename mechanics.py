import time
import tabulate
from color_configs import *
def fight_monster_melee(player:list,monster:list):
    import random

    player_name = player[0]
    player_damage = player[1]
    player_hp = player[2]
    player_bonus_damage = player[3]
    player_bonus_hp = player[4]

    player_damage_overall = player_damage + player_bonus_damage
    player_health_overall = player_hp + player_bonus_hp

    monster_name = monster[0]
    monster_hp = monster[2]
    monster_damage = monster[3]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_health_overall > 0) and (monster_hp > 0):
        if has_first_go_player:
            print(f"{FIGHT_PLAYER}{player_name} атакует!{DEFAULT_COLOR}\n{'-'*20}")
            monster_hp -= player_damage_overall
            has_first_go_player = False
            if monster_hp < 0:
                monster_hp = 0
            print(f"{FIGHT_PLAYER}{monster_name} осталось {monster_hp} здоровья{DEFAULT_COLOR}\n{'-'*20}")
            time.sleep(1)
        else:
            print(F"{FIGHT_MONSTER}Монстр атакует!{DEFAULT_COLOR}\n{'-'*20}")
            player_health_overall -= monster_damage
            if player_health_overall < 0:
                player_health_overall = 0
            has_first_go_player = True
            print(f"{FIGHT_MONSTER}{player_name} осталось {player_health_overall} здоровья{DEFAULT_COLOR}\n{'-'*20}")
        time.sleep(1)

    if player_health_overall > 0:
        print(f"{FIGHT_PLAYER}{player_name} одержал победу!{DEFAULT_COLOR}")
        return True

    if monster_hp > 0:
        print(f"{FIGHT_MONSTER}Монстр {monster_name} одержал победу!{DEFAULT_COLOR}")
        return False
    


def open_loot_box(current_player,items):
    import time
    print(f"{LOOTBOX_COLOR}Вы открываете сундук{DEFAULT_COLOR}")
    time.sleep(1)

    data = [
    ["тип предмета","Название предмета","Количество усиления"],
    [items[0][0],items[0][1],items[0][2]],
    [items[1][0],items[1][1],items[1][2]],
    [items[2][0],items[2][1],items[2][2]],
    [items[3][0],items[3][1],items[3][2]],
    ]

    output = tabulate.tabulate(data)
    print(output)
    choice = int(input(f"\n{SYSTEM_COLOR}System >> {LOOTBOX_COLOR}Введите номер предмета(5 чтобы пропустить):{DEFAULT_COLOR}"))


    if choice == 1:
        item = items[0]

    elif choice == 2:
        item = items[1]

    elif choice == 3:
        item = items[2]

    elif choice == 4:
        item = items[3]

    elif choice == 5:
        return current_player
    
    if item[0][0] == "health":
        player = [current_player[0],current_player[1],item[2][0],current_player[3],current_player[4]]

    elif item[0][0] == "damage":
        player = [current_player[0],item[2][0],current_player[2],current_player[3],current_player[4]]

    elif item[0][0] == "health_bonus":
        player = [current_player[0],current_player[1],current_player[2],current_player[3],item[2][0]]

    return player

def fight_monster_ranged(player:list, ranged_monster:list):
    import time
    import random

    player_name = player[0]
    player_damage = player[1]
    player_hp = player[2]
    player_bonus_damage = player[3]
    player_bonus_hp = player[4]
    
    player_damage_overall = player_damage + player_bonus_damage
    player_health_overall = player_hp + player_bonus_hp

    monster_ranged_name = ranged_monster[0]
    monster_ranged_hp = ranged_monster[2]
    monster_ranged_damage = ranged_monster[3]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_health_overall > 0) and (monster_ranged_hp > 0):
        if has_first_go_player:
            if random.randint(0,100) >= 80:
                print(f"{FIGHT_PLAYER}{player_name} атакует... но промахивается!{DEFAULT_COLOR}\n{'-'*20}")
                has_first_go_player = False
                time.sleep(1)
                continue
            print(f"{FIGHT_PLAYER}{player_name} атакует!{DEFAULT_COLOR}\n{'-'*20}")
            monster_ranged_hp -= player_damage_overall
            has_first_go_player = False
            if monster_ranged_hp < 0:
                monster_ranged_hp = 0
            print(f"{FIGHT_PLAYER}{monster_ranged_name} осталось {monster_ranged_hp} здоровья{DEFAULT_COLOR}\n{'-'*20}")
            time.sleep(1)
        else:
            print(F"{FIGHT_MONSTER}Монстр атакует!{DEFAULT_COLOR}\n{'-'*20}")
            player_health_overall -= monster_ranged_damage
            has_first_go_player = True
            if player_health_overall < 0:
                player_health_overall = 0
            print(f"{FIGHT_MONSTER}{player_name} осталось {player_health_overall} здоровья{DEFAULT_COLOR}\n{'-'*20}")
        time.sleep(1)

    if player_health_overall > 0:
        print(f"{FIGHT_PLAYER}{player_name} одержал победу!{DEFAULT_COLOR}")
        return True

    if monster_ranged_hp > 0:
        print(f"{FIGHT_MONSTER}Монстр {monster_ranged_name} одержал победу!{DEFAULT_COLOR}")
        return False

def fight_boss(player,boss):
    import time
    import random

    player_name = player[0]
    player_damage = player[1]
    player_hp = player[2]
    player_bonus_damage = player[3]
    player_bonus_hp = player[4]
    
    player_damage_overall = player_damage + player_bonus_damage
    player_health_overall = player_hp + player_bonus_hp

    boss_name = boss[0]
    boss_hp = boss[1]
    boss_damage = boss[2]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_health_overall > 0) and (boss_hp > 0):
        if has_first_go_player:
            print(f"{FIGHT_PLAYER}{player_name} атакует!{DEFAULT_COLOR}\n{'-'*20}")
            boss_hp -= player_damage_overall
            has_first_go_player = False

            if boss_hp < 0:
                boss_hp = 0
            print(f"{FIGHT_PLAYER}{boss_name} осталось {boss_hp} здоровья{DEFAULT_COLOR}\n{'-'*20}")
            time.sleep(1)

        else:
            print(F"{FIGHT_MONSTER}Монстр атакует!{DEFAULT_COLOR}")
            player_health_overall -= boss_damage
            has_first_go_player = True

            if player_health_overall < 0:
                player_health_overall = 0
            print(f"{FIGHT_MONSTER}{player_name} осталось {player_health_overall} здоровья{DEFAULT_COLOR}\n{'-'*20}")

        time.sleep(1)

    if player_health_overall > 0:
        print(f"{FIGHT_PLAYER}{player_name} одержал победу!{DEFAULT_COLOR}")
        return True

    if boss_hp > 0:
        print(f"{FIGHT_MONSTER}Монстр {boss_name} одержал победу!{DEFAULT_COLOR}")
        return False