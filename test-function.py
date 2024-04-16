import json
import math
import numpy as np
import time as t
import os
import hashlib
file_paths = {0: 'bonus_stats_Physical.json', 1: 'bonus_stats_Magic.json', 2: 'bonus_stats_Defense.json', 3: 'bonus_stats_Hybrid.json'}

def import_data(path):
    with open(path, 'r') as jsonReader:
        return json.load(jsonReader)

__number_of_bs = {
        0: [1, 2],
        1: [2, 3],
        2: [4, 5],
        3: [5, 6],
        4: 6,
        5: 6
    }
rng = np.random.default_rng(seed=int(t.time()))
type_switcher = {
        0: file_paths[0],
        1: file_paths[1],
        2: file_paths[2],
        3: file_paths[3]
    }

__number_of_bs = {
        0: [1, 2],
        1: [2, 3],
        2: [3, 4],
        3: [5, 6],
        4: [6, 6],
        5: [6, 6]
    }
seed = int(hashlib.sha256(os.urandom(32)).hexdigest(), 16)
rkl = np.random.default_rng(seed=seed)


def main():
    data = import_data(type_switcher.get(1))
    stats_pool = data['bonus-stats']
    upper_threshold = stats_pool[-1]['id'] + 1  # Get count of all bonus stats in file
    print(upper_threshold)
    # Get random number of bonus stats from rarity ( 0 and 1 as the range from-to )
    number_of_bonus_stats = __number_of_bs.get(5)[np.random.randint(2)]
    selected_id = rng.choice(upper_threshold, number_of_bonus_stats, replace=False)
    for i in selected_id:
        print(i)
    bonus_stats = []
    print(stats_pool)
    for _ in selected_id:
        stat = next((s for s in stats_pool if s['id'] == _))
        if stat:
            stat_name = stat['name']
            value_range = stat['value_range']
            generated_value = rng.integers(value_range[0], value_range[1]+1)
            bonus_stats.append([stat_name, _, generated_value])
    print(bonus_stats)
    for _ in bonus_stats:
        print('_ ' + str(_[0]) + ': +' + str(_[2]))


main()