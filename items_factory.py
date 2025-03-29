def generate_items():
    import itemsconfigs
    import random
    items = []
    for i in range(0,4,1):
        item_type = random.randint(0,2)
        if item_type == 0:
            item = ["health",itemsconfigs.NAMES_ITEM_HEALTH[random.randint(0,3)],itemsconfigs.ITEMS_HEALTH[random.randint(0,3)]]
        if item_type == 1:
            item = ["damage",itemsconfigs.NAMES_ITEM_DAMAGE[random.randint(0,5)],itemsconfigs.ITEMS_DAMAGE[random.randint(0,5)]]
        else:
            item = item = ["health_bonus",itemsconfigs.NAMES_ITEM_BONUS_HEALTH[random.randint(0,3)],itemsconfigs.ITEMS_BONUS_HEALTH[random.randint(0,3)]]
        items.append(item)
    return items


