import time

def fight_monster_melee(player: list[int, int], monster: list[str, int, int]):
    import random

    player_hp = player[0]
    player_damage = player[1]

    monster_name = monster[0]
    monster_hp = monster[1]
    monster_damage = monster[2]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_hp > 0) and (monster_hp > 0):
        if has_first_go_player:
            print("Герой атакует!")
            monster_hp -= player_damage
            has_first_go_player = False
            print(f"{monster_name} осталось {monster_hp} здоровья")
        else:
            print("Монстр атакует!")
            player_hp -= monster_damage
            has_first_go_player = True
            print(f"игрок осталось {player_hp} здоровья")
        time.sleep(0.5)

    if player_hp > 0:
        return "Игрок одержал победу!"

    if monster_hp > 0:
        print(f"Монстр {monster_name} одержал победу!")
        return exit(0)
        


def loot_box(NAMES_ITEMS_DAMAGE,NAMES_ITEMS_HEALTH,ITEMS_DAMAGE,ITEMS_HEALTH,damage,skill,damage_list,health,health_list):
    import time
    import random
    from enteties_factory import create_players

    print("После победы над монстром вы находите сундук")
    time.sleep(1)

    item_type = random.randint(0,1)
    if item_type == 0:
        item_health = 0
        item_name = NAMES_ITEMS_DAMAGE[random.randint(0,5)]
        item_damage = ITEMS_DAMAGE[random.randint(0,5)]

        print("Открывается сундук")
        time.sleep(1)

        print(f"Вы находите {item_name} Количество урона:{item_damage}")

    if item_type == 1:
        item_damage = 0
        item_name = NAMES_ITEMS_HEALTH[random.randint(0,3)]
        item_health = ITEMS_HEALTH[random.randint(0,3)]

        print("Открывается сундук")
        time.sleep(1)

        print(f"Вы находите {item_name} Количество жизней:{item_health}")
        time.sleep(3)

    health_sum = health + item_health
    health_list = []
    health_list.append(health_sum)

    sum_damage = damage + skill + item_damage
    damage_list = []
    damage_list.append(sum_damage)
    player = create_players(health_sum,sum_damage)

    return player

def lvl(current_level):
    current_level =+ 1
    return current_level

def fight_monster_ranged(player: list[int, int], ranged_monster: list[str, int, int]):
    import time
    import random
    import monstersconfigs
    player_hp = player[0]
    player_damage = player[1]

    monster_ranged_name = ranged_monster[0]
    monster_ranged_hp = ranged_monster[1]
    monster_ranged_damage = ranged_monster[2]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_hp > 0) and (monster_ranged_hp > 0):
        if has_first_go_player:
            if random.randint(0,100) >= 70:
                print("Герой атакует... но промахивается!")
                has_first_go_player = False
                continue
            print("Герой атакует!")
            monster_ranged_hp -= player_damage
            has_first_go_player = False
            print(f"{monster_ranged_name} осталось {monster_ranged_hp} здоровья")
        else:
            print("Монстр атакует!")
            player_hp -= monster_ranged_damage
            has_first_go_player = True
            print(f"игрок осталось {player_hp} здоровья")
        time.sleep(0.5)

    if player_hp > 0:
        return "Игрок одержал победу!"

    if monster_ranged_hp > 0:
        print(f"Монстр {monster_ranged_name} одержал победу!")
        return exit(0)
