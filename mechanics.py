import time

def class_selection():
   print("Выберите свой класс \nмаг 0 чтоб выбрать(8 урона 60 жизней 5 бонусного урона 6 бонусных жизней)\n---------------\nрыцарь 1 чтоб выбрать(5 урона 80 жизней 3 бонусного урона 8 бонусных жизней)\n---------------\nохотник 2 чтоб выбрать(6 урона 75 жизней 3 бонусного урона 6 бонусных жизней)\n---------------\nассасин 3 чтоб выбрать(8 урона 65 жизней 3 бонусного урона 8 бонусных жизней)\n---------------\nпаладин 4 чтоб выбрать(3 урона 90 жизней 4 бонусного урона 6 бонусных жизней)")
   player_class = int(input())
   return player_class

def fight_monster_melee(player:list,monster:list):
    import random

    player_name = player[0]
    player_hp = player[1]
    player_damage = player[2]
    player_bonus_damage = player[3]
    player_bonus_hp = player[4]

    player_damage_overall = player_damage + player_bonus_damage
    player_health_overall = player_hp + player_bonus_hp

    monster_name = monster[0]
    monster_hp = monster[1]
    monster_damage = monster[2]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_health_overall > 0) and (monster_hp > 0):
        if has_first_go_player:
            print(f"{player_name} атакует!")
            monster_hp -= player_damage_overall
            has_first_go_player = False
            print(f"{monster_name} осталось {monster_hp} здоровья")
        else:
            print("Монстр атакует!")
            player_health_overall -= monster_damage
            has_first_go_player = True
            print(f"{player_name} осталось {player_hp} здоровья")
        time.sleep(0.5)

    if player_hp > 0:
        return f"{player_name} одержал победу!"

    if monster_hp > 0:
        print(f"Монстр {monster_name} одержал победу!")
        return exit(0)


def open_loot_box(current_player,items):
    import time
    print("Вы находите сундук")
    time.sleep(1)

    choice = int(input(f"в сундуке 4 предмета {items[0]}\n,{items[1]}\n,{items[2]}\n,{items[3]}\n,но вы можете выбрать только один(выберите номер предмета,5 чтобы пропустить выбор) >>"))

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
    player_hp = player[1]
    player_damage = player[2]
    player_bonus_damage = player[3]
    player_bonus_hp = player[4]
    
    player_damage_overall = player_damage + player_bonus_damage
    player_health_overall = player_hp + player_bonus_hp

    monster_ranged_name = ranged_monster[0]
    monster_ranged_hp = ranged_monster[1]
    monster_ranged_damage = ranged_monster[2]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_health_overall > 0) and (monster_ranged_hp > 0):
        if has_first_go_player:
            if random.randint(0,100) >= 70:
                print(f"{player_name} атакует... но промахивается!")
                has_first_go_player = False
                continue
            print(f"{player_name} атакует!")
            monster_ranged_hp -= player_damage_overall
            has_first_go_player = False
            print(f"{monster_ranged_name} осталось {monster_ranged_hp} здоровья")
        else:
            print("Монстр атакует!")
            player_health_overall -= monster_ranged_damage
            has_first_go_player = True
            print(f"{player_name} осталось {player_hp} здоровья")
        time.sleep(0.5)

    if player_hp > 0:
        return f"{player_name} одержал победу!"

    if monster_ranged_hp > 0:
        print(f"Монстр {monster_ranged_name} одержал победу!")
        return exit(0)

def fight_boss(player,boss):
    pass