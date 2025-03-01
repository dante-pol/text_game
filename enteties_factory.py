def create_players(health_list,damage_list):
    player = [health_list,damage_list]
    return player

def create_monster() -> list[str, int, int]:
    import monstersconfigs
    import random

    name = monstersconfigs.NAMES[random.randint(0, len(monstersconfigs.NAMES)-1)]
    hp = monstersconfigs.HEAT_POINTS[random.randint(0, len(monstersconfigs.HEAT_POINTS)-1)]
    damage = monstersconfigs.DAMAGES[random.randint(0, len(monstersconfigs.DAMAGES)-1)]

    monster = [name, hp, damage]

    return monster


