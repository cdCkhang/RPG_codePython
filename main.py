import json as js
from item_class import Item as ic
from numpy.random import MT19937
from numpy.random import RandomState


file_paths = {0: 'bonus_stats_Physical.json', 1: 'bonus_stats_Magic.json', 2: 'bonus_stats_Hybrid.json', 3: 'bonus_stats_Defense.json'}
rarity_to_bonus_stats = {"C": 1, "R": [1, 2], "E": [2, 3], "L": [3, 4], "M": [5, 6], "D": 6}
list_of_items = {}


def input_an_item():
    n = int(input("Enter item's type ( 0-Phys / 1-Mgc / 2-Hyb /3-Def ) : "))
    m = int(input("Enter item's rarity ( 0-Bs ,1-Rr, 2-Ep, 3-Leg, 4-Myth, 5-Div ):"))


def generate_an_item(rarity):
    data = import_data(file_paths[1])
    bs = data['bonus-stats']
    upperthreshold = bs[-1]['id']+1
    for i in bs:
        if i['id'] == 2:
            print(i['name'])


def import_data(file):
    with open(file, 'r') as JsonReader:
        data = js.load(JsonReader)
    return data


newItem = ic("ca", 3, {1: 3}, 12, 0, 2, [30, 30], [0, 100], [{1: 30}, {0: 100}], [{7: 40}, {4: 35}, {2: 12}], {0: 1},
              [(1, 2), (0, 0)])


if __name__ == '__main__':
    print(ic.number_to_rarity(newItem.GetItemAttribute["rarity"]))
    import_data(file_paths[0])

