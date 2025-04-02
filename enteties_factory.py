def create_players(name,player_class):
    import playerconfigs
    damage =playerconfigs.DAMAGE[player_class]
    health = playerconfigs.HEALTH[player_class]
    bonus_damage =playerconfigs.BONUS_DAMAGE[player_class]
    bonus_heath =playerconfigs.BONUS_HEALTH[player_class]
    player = [name,damage,health,bonus_damage,bonus_heath]
    return player

def create_stage(player):
    import random
    import roomconfigs as rc
    
    stage_index = random.randint(0,len(rc.stages)-1)
    config = rc.stages[stage_index]
    stage = []

    for room in config:
        if room == rc.MONSTER:
            id, monster = create_monster()
            if id == 3:
              stage.append(rc.MELEE)  
            else:
                stage.append(rc.RANGE)
            
    
        elif room == rc.LOOTBOX:
            stage.append(rc.LOOTBOX,create_loot_box(player))

        elif room == rc.BOSS:
            stage.append(rc.BOSS,create_boss())
    return stage
def create_monster():
    import random
    import roomconfigs as rc

    monster_probability = random.randint(0,100)
    melee_probability = 50

    if monster_probability <= melee_probability:
        return rc.MELEE,__create_monster_melee()
    
    else:
        return rc.RANGE,__create_ranged_monster()

def create_boss():
    boss = __create_monster_boss()
    return boss

def create_loot_box(player):
    from mechanics import loot_box
    new_player = loot_box()
    return new_player

def __create_monster_boss():
    import monstersconfigs as mc
    import random 
    name = mc.NAMES_BOSS[random.randint(0,len(mc.NAMES_BOSS)- 1)]
    hp = mc.HEAT_POINTS_BOSS[random.randint(0, len(mc.HEAT_POINTS_BOSS) - 1)]
    damage = mc.DAMAGE_BOSS[random.randint(0, len(mc.DAMAGE_BOSS) - 1)]

    boss = [name,hp,damage]

    return boss

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

