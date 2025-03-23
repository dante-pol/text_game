def create_players(name,player_class):
    import playerconfigs
    player = [name,playerconfigs.DAMAGE[player_class],playerconfigs.HEALTH[player_class],playerconfigs.BONUS_DAMAGE[player_class],playerconfigs.BONUS_HEALTH[player_class]]
    return player

def create_monster():
    import random

    monster_probability = random.randint(0,100)
    melee_probability = 50

    if monster_probability <= melee_probability:
        return __create_monster_melee()
    
    else:
        return __create_ranged_monster()

def create_boss():
    pass

def create_loot_box(player):
    from mechanics import loot_box
    new_player = loot_box(player)
    return new_player

def __create_monster_melee() -> list[str, int, int, int]:
    import monstersconfigs
    import random

    name = monstersconfigs.NAMES_MELEE[random.randint(0, len(monstersconfigs.NAMES_MELEE) - 1)]
    level = monstersconfigs.LEVEL_MELEE[random.randint(0, len(monstersconfigs.LEVEL_MELEE) - 1)]
    hp = monstersconfigs.HEAT_POINTS_MELEE[random.randint(0, len(monstersconfigs.HEAT_POINTS_MELEE) - 1)]
    damage = monstersconfigs.DAMAGES_MELEE[random.randint(0, len(monstersconfigs.DAMAGES_MELEE) - 1)]

    monster = [name, level, hp, damage]

    return monster

def __create_ranged_monster():
    import monstersconfigs
    import random

    name_ranged = monstersconfigs.NAMES_RANGED[random.randint(0, len(monstersconfigs.NAMES_RANGED)-1)]
    level_ranged = monstersconfigs.LEVEL_RANGED[random.randint(0, len(monstersconfigs.LEVEL_RANGED) - 1)]
    hp_ranged = monstersconfigs.HEAT_POINTS_RANGED[random.randint(0, len(monstersconfigs.HEAT_POINTS_RANGED)-1)]
    damage_ranged = monstersconfigs.DAMAGES_RANGED[random.randint(0, len(monstersconfigs.DAMAGES_RANGED)-1)]

    ranged_monster = [name_ranged, level_ranged,hp_ranged, damage_ranged]

    return ranged_monster

def create_door(is_boss: bool = False):
    import random

    if is_boss:
        return create_boss()

    loot_box_probability = random.randint(0, 100)
    monster_limit_right = 70

    if loot_box_probability > monster_limit_right:
        return create_loot_box()
    else:
        return create_monster()
