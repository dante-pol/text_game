import time


def fight_monster_melee(player: list[int, int], monster: list[str, int, int]):
    import random

    player_hp = player[0]
    player_damage = player[1]

    monster_name = monster[0]
    monster_hp = monster[1]
    monster_damage = monster[2]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_hp > 0) or (monster_hp > 0):
        if has_first_go_player:
            print("Герой атакует!")
            monster_hp -= player_damage
            has_first_go_player = False
        else:
            print("Монстр атакует!")
            player_hp -= monster_damage
            has_first_go_player = True
        time.sleep(0.1)

    if player_hp > 0:
        return "Игрок одержал победу!"

    if monster_hp > 0:
        return f"Монстр {monster_name} одержал победу!"


def loot_box(items: list[str, ...]) -> None or str:
    import random
    import time

    is_lucky_loot = random.randint(0, 100) > 80

    for i in range(0, 101, 1):
        if not is_lucky_loot and i == 98:
            return None

        print(f"looting progress {i}%...")
        time.sleep(0.15)

    if is_lucky_loot:
        item_index = random.randint(0, len(items))
        return items[item_index]