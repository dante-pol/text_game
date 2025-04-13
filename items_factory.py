import itemsconfigs
import random

def generate_items():
    num_of_items = 4
    items = []

    for i in range(0,num_of_items,1):
        item_type = random.randint(0,2)

        if item_type == 0:
            item = create_item_health()

        elif item_type == 1:
            item = create_item_damage()

        else:
            item = create_item_bonus_health()
        items.append(item)
    return items

def create_item_damage():

    item = ["damage",itemsconfigs.NAMES_ITEM_DAMAGE[random.randint(0,5)],itemsconfigs.ITEMS_DAMAGE[random.randint(0,5)]]
    return item

def create_item_health():

    item = ["health",itemsconfigs.NAMES_ITEM_HEALTH[random.randint(0,3)],itemsconfigs.ITEMS_HEALTH[random.randint(0,3)]]
    return item

def create_item_bonus_health():

    item = ["health_bonus",itemsconfigs.NAMES_ITEM_BONUS_HEALTH[random.randint(0,3)],itemsconfigs.ITEMS_BONUS_HEALTH[random.randint(0,3)]]
    return item