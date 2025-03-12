from mechanics import *
from enteties_factory import *
from itemsconfigs import *
#жизни от 0 до 100 урон от 1 до 15 бонус к урону от 1 - 7
print("Приветствуем в нашей текстовой игре")

player_name = input("Как вас зовут >>")
print("Выберите свое снаряжение >> ")

damage_list = []
health_list = []


weapon = int(input("Выбор оружия\n1.обычный меч\n2.пистолет\n3.посох мага\n------\n"))

def count_damage(weapon):
    if weapon == 1:
        damage = 7

    if weapon == 2:
        damage = 12

    if weapon == 3:
        damage = 5

    return damage

armor = int(input("Выбор брони\n1.Латная броня\n2.бронежилет\n3.роба мага\n------\n"))

def count_health(armor):
    if armor == 1:
        health = 100

    if armor == 2:
        health = 70

    if armor == 3:
        health = 40

    return health

skill = int(input("Выбор способности\n1.усиление физических показателей\n2.ускоренная перезарядка\n3.знание начальных заклинаний\n------\n"))

def count_bonus_damage(skill):
    if skill == 1:
        bonus_damage = 5

    if skill == 2:
        bonus_damage = 3

    if skill == 3:
        bonus_damage = 7

    return bonus_damage

accessory = int(input("Выбор аксессуара\n1.кожаный рюкзак\n2.кобура\n3.кольцо маны\n------\n"))

def count_bonus_health(accessory):
    if accessory == 1:
        bonus_health = 5

    if accessory == 2:
        bonus_health = 7

    if accessory == 3:
        bonus_health = 3

    return bonus_health

damage = count_damage(weapon)
health = count_health(armor)
bonus_damage = count_bonus_damage(skill)
bonus_health = count_bonus_health(accessory)



