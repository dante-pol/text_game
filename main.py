#жизни от 0 до 100 урон от 1 до 15 бонус к урону от 1 - 7
print("Приветствуем в нашей текстовой игре")

print("Выберите свое снаряжение")

damage_list = []
health_list = []
selection = []

weapon = int(input("Выбор оружия\n1.обычный меч\n2.пистолет\n3.посох мага"))
selection.append(weapon)

def count_damage(weapon):
    if weapon == 1:
        damage = 7

    if weapon == 2:
        damage = 12

    if weapon == 3:
        damage = 5

    return damage

armor = int(input("Выбор брони\n1.Латная броня\n2.бронежилет\n3.роба мага"))
selection.append(armor)

def count_health(armor):
    if armor == 1:
        health = 100

    if armor == 2:
        health = 70

    if armor == 3:
        health = 40

    return health

skill = int(input("Выбор способности\n1.усиление физических показателей\n2.ускоренная перезарядка\n3.знание начальных заклинаний"))
selection.append(skill)

def count_bonus_damage(skill):
    if skill == 1:
        bonus_damage = 5

    if skill == 2:
        bonus_damage = 3

    if skill == 3:
        bonus_damage = 7

    return bonus_damage

sum_damage = count_damage(weapon) + count_bonus_damage(skill)
damage_list.append(sum_damage)

health_list.append(count_health(armor))
def fight_monster_melee(player: list[int, int], monster: list[int, int]):
    import random

    player_hp = player[0]
    player_damage = player[1]

    monster_hp = monster[0]
    monster_damage = monster[1]

    has_first_go_player = True if random.randint(0, 100) > 60 else False

    while (player_hp > 0) or (monster_hp > 0):
        if has_first_go_player:
            monster_hp -= player_damage
            has_first_go_player = False
        else:
            player_hp -= monster_damage
            has_first_go_player = True

    if player_hp > 0:
        return "Игрок одержал победу!"

    if monster_hp > 0:
        return "Монстр одержал победу!"


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