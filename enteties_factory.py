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


