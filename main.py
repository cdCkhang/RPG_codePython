import json as js
from item_class import Item as ic
from numpy.random import MT19937
from numpy.random import RandomState


file_paths = {0: 'bonus_stats_Physical.json', 1: 'bonus_stats_Magic.json', 2: 'bonus_stats_Hybrid.json', 3: 'bonus_stats_Defense.json'}
rarity_to_bonus_stats = {"C": 1, "R": [1, 2], "E": [2, 3], "L": [3, 4], "M": [5, 6], "D": 6}
list_of_items = {}


def input_an_item() -> [int]:
    item_type = int(input("Enter item's type ( 0-Phys / 1-Mgc / 2-Hyb /3-Def ) : "))
    item_rarity = int(input("Enter item's rarity ( 0-Bs ,1-Rr, 2-Ep, 3-Leg, 4-Myth, 5-Div ):"))
    item_upgrades = int(input("Enter item's number of upgrades : "))
    item_star = int(input("Enter item's star level : "))
    return{
        item_type, item_rarity, item_upgrades, item_star
    }


def generate_an_item(user_inp: [int]) -> ic:
    data = import_data(file_paths[1])
    bonus_stats_pool = data['bonus-stats']
    upperthreshold = bonus_stats_pool[-1]['id']+1
    for i in bonus_stats_pool:
        if i['id'] == 2:
            print(i['name'])
    newitem = ic("12")
    return newitem


def import_data(file):
    with open(file, 'r') as JsonReader:
        data = js.load(JsonReader)
    return data


if __name__ == '__main__':
    newItem = ic("ca", 3, {1: 3}, 12, 4, 2, [30, 30], [0, 100], [{1: 30}, {0: 100}], [{7: 40}, {4: 35}, {2: 12}],{0: 1})
    print(newItem.__getitem__()["rarity"])
    print(newItem.__getitem__()["refinements"])
    print(ic.rarity_mapping(newItem.GetItemAttribute["rarity"]))
    print(newItem.__getitem__()["star"])
    import_data(file_paths[0])

