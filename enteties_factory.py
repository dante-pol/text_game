def create_players(health_list,damage_list):
    player = [health_list,damage_list]
    return player

def create_monster_melee() -> list[str, int, int, int]:
    import monstersconfigs
    import random

    name = monstersconfigs.NAMES_MELEE[random.randint(0, len(monstersconfigs.NAMES_MELEE) - 1)]
    level = monstersconfigs.LEVEL_MELEE[random.randint(0, len(monstersconfigs.LEVEL_MELEE) - 1)]
    hp = monstersconfigs.HEAT_POINTS_MELEE[random.randint(0, len(monstersconfigs.HEAT_POINTS_MELEE) - 1)]
    damage = monstersconfigs.DAMAGES_MELEE[random.randint(0, len(monstersconfigs.DAMAGES_MELEE) - 1)]

    monster = [name, level, hp, damage]

    return monster

def create_ranged_monster():
    import monstersconfigs
    import random

    name_ranged = monstersconfigs.NAMES_RANGED[random.randint(0, len(monstersconfigs.NAMES_RANGED)-1)]
    hp_ranged = monstersconfigs.HEAT_POINTS_RANGED[random.randint(0, len(monstersconfigs.HEAT_POINTS_RANGED)-1)]
    damage_ranged = monstersconfigs.DAMAGES_RANGED[random.randint(0, len(monstersconfigs.DAMAGES_RANGED)-1)]

    ranged_monster = [name_ranged, hp_ranged, damage_ranged]

    return ranged_monster

