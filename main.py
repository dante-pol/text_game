from mechanics import *
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

def create_players(health_list,damage_list):
    player = [[health_list],[damage_list]]
    return player

def create_monster() -> list[str, int, int]:
    import monstersconfigs
    import random

    name = monstersconfigs.NAMES[random.randint(0, monstersconfigs.NAMES)]
    hp = monstersconfigs.HEAT_POINTS[random.randint(0, monstersconfigs.HEAT_POINTS)]
    damage = monstersconfigs.DAMAGES[random.randint(0, monstersconfigs.DAMAGES)]

    monster = [name, hp, damage]

    return monster


