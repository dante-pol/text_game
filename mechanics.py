import time

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

def loot_box(player):
    import time
    import random
    from enteties_factory import create_players
    import monstersconfigs

    print("После победы над монстром вы находите сундук")
    time.sleep(1)

    item_type = random.randint(0,1)
    if item_type == 0:
        item_name = monstersconfigs.NAMES_ITEMS_DAMAGE[random.randint(0,5)]
        item_damage = monstersconfigs.ITEMS_DAMAGE[random.randint(0,5)]

        print("Открывается сундук")
        time.sleep(1)

        print(f"Вы находите {item_name} Количество урона:{item_damage}")

    if item_type == 1:
        item_name = monstersconfigs.NAMES_ITEMS_HEALTH[random.randint(0,3)]
        item_health = monstersconfigs.ITEMS_HEALTH[random.randint(0,3)]

        print("Открывается сундук")
        time.sleep(1)

        print(f"Вы находите {item_name} Количество жизней:{item_health}")
        time.sleep(3)

    health = player[0][1] + item_health
    damage = player[0][0] + player[0][2] + item_damage
    player = create_players(damage,health,player[0][2],player[0][3])

    return player

def lvl(current_level):
    current_level =+ 1
    return current_level

def fight_monster_ranged(player:list, ranged_monster:list):
    import time
    import random
    import monstersconfigs
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
