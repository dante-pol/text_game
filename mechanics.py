import time

def class_selection():
   print("Выберите свой класс \nмаг 0 чтоб выбрать(8 урона 60 жизней 5 бонусного урона 6 бонусных жизней)\n---------------\nрыцарь 1 чтоб выбрать(5 урона 80 жизней 3 бонусного урона 8 бонусных жизней)\n---------------\nохотник 2 чтоб выбрать(6 урона 75 жизней 3 бонусного урона 6 бонусных жизней)\n---------------\nассасин 3 чтоб выбрать(8 урона 65 жизней 3 бонусного урона 8 бонусных жизней)\n---------------\nпаладин 4 чтоб выбрать(3 урона 90 жизней 4 бонусного урона 6 бонусных жизней)")
   player_class = int(input())
   return player_class

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
            print(f"{player_name} атакует!")
            monster_hp -= player_damage_overall
            has_first_go_player = False
            if monster_hp < 0:
                monster_hp = 0
            print(f"{monster_name} осталось {monster_hp} здоровья")
        else:
            print("Монстр атакует!")
            player_health_overall -= monster_damage
            if player_health_overall < 0:
                player_health_overall = 0
            has_first_go_player = True
            print(f"{player_name} осталось {player_health_overall} здоровья")
        time.sleep(0.5)

    if player_health_overall > 0:
        print(f"{player_name} одержал победу!")
        return True

    if monster_hp > 0:
        print(f"Монстр {monster_name} одержал победу!")
        return False


def open_loot_box(current_player,items):
    import time
    print("Вы открываете сундук")
    time.sleep(1)

    print(f"в сундуке 4 предмета\n{'-'*20}\n{items[0]}\n{'-'*20}\n{items[1]}\n{'-'*20}\n{items[2]}\n{'-'*20}\n{items[3]}\nно вы можете выбрать только один(выберите номер предмета,5 чтобы пропустить выбор)")
    choice = int(input())
    if choice == 1:
        item = items[0]

    if choice == 2:
        item = items[1]

    if choice == 3:
        item == items[2]

    if choice == 4:
        item = items[3]

    if choice == 5:
        return current_player
    
    if item[0] == "health":
        player = [current_player[0],current_player[1],item[2],current_player[3],current_player[4]]

    if item[0] == "damage":
        player = [current_player[0],item[2],current_player[3],current_player[4]]

    if item[0] == "health_bonus":
        player = [current_player[0],current_player[1],current_player[2],current_player[3],item[2]]

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
                print(f"{player_name} атакует... но промахивается!")
                has_first_go_player = False
                continue
            print(f"{player_name} атакует!")
            monster_ranged_hp -= player_damage_overall
            has_first_go_player = False
            if monster_ranged_hp < 0:
                monster_ranged_hp = 0
            print(f"{monster_ranged_name} осталось {monster_ranged_hp} здоровья")
        else:
            print("Монстр атакует!")
            player_health_overall -= monster_ranged_damage
            has_first_go_player = True
            if player_health_overall < 0:
                player_health_overall = 0
            print(f"{player_name} осталось {player_health_overall} здоровья")
        time.sleep(0.5)

    if player_health_overall > 0:
        print(f"{player_name} одержал победу!")
        return True

    if monster_ranged_hp > 0:
        print(f"Монстр {monster_ranged_name} одержал победу!")
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
            print(f"{player_name} атакует!")
            boss_hp -= player_damage_overall
            has_first_go_player = False

            if boss_hp < 0:
                boss_hp = 0
            print(f"{boss_name} осталось {boss_hp} здоровья")

        else:
            print("Монстр атакует!")
            player_health_overall -= boss_damage
            has_first_go_player = True

            if player_health_overall < 0:
                player_health_overall = 0
            print(f"{player_name} осталось {player_health_overall} здоровья")

        time.sleep(0.5)

    if player_health_overall > 0:
        print(f"{player_name} одержал победу!")
        return True

    if boss_hp > 0:
        print(f"Монстр {boss_name} одержал победу!")
        return False