import os
import math
import hashlib
import numpy as np
import json as js
import time
file_paths = {0: 'bonus_stats_Physical.json',
              1: 'bonus_stats_Magic.json',
              2: 'bonus_stats_Defense.json',
              3: 'bonus_stats_Hybrid.json'}


class Item:
    _Item_name: str = ""
    _Item_type: int = 0
    _Item_level: int = 0
    _Item_tier: int = 0
    _Item_rarity: int = 0  # Ex : 1 - Rare
    _Item_grade: list[int, float] = [0, 0] # Ex : 1[grade] - 9[value] ==> Excellent : +9% base stats
    _Item_upgrades: int = 0
    _Item_star_crafted: int = 0
    _Item_element_type: int = 0
    _Item_durability: list = [0, 0]  # Ex : 30,30 ==> Dur : 30/50
    _Item_mastery: list = [0, 0]  # Ex : 40,100 ==> Mas : 40/100
    _Item_base_stats: list[list[int, int]] = [(0, 0)]  # Ex : 1[id], 130[value] ==> Physical attack : +130
    # Ex : 4[id], 40[value], "Physical armor penetration"[name] ==> Physical armor penetration : +40
    _Item_bonus_stats: list[list[int, int, str]] = [(0, 0, "")]
    _Item_unique: dict = {0: 0}  # Ex : 1[id], 2[value/level] ==> Increase basic attack damage by %
    _Item_refinements: list[list[int, int, str]] = [(0, 0, ""), (0, 0, "")]  # Ex : [(1,2),(2,3)] ==> Ref id#1 level 2, Ref id#2 level 3

    __item_type = {
        0: "Physical", 1: "Magic", 2: "Defensive", 3: "Hybrid"
    }
    __dur_multiplier = {
        0: 15, 1: 16, 2: 17, 3: 18, 4: 19, 5: 20
    }
    __rarity_name = {
        0: "Basic", 1: "Rare", 2: "Epic", 3: "Legendary", 4: "Mythic", 5: "Divine"
    }
    __number_of_bs = {
        0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [5, 6], 4: [6, 7], 5: [7, 7]
    }
    __grade_name = {
        0: "Standard", 1: "Fine", 2: "Excellent", 3: "Perfect", 4: "Supreme",
    }
    __grade_value_multiplier = {
        0: 1.0,   # No bonus
        1: 1.03,  # 3% base stats
        2: 1.06,  # 6% base stats
        3: 1.09,  # 9% base stats
        4: 1.12   # 12% base stats
    }
    __eletype = {
        0: "Fire", 1: "Water", 2: "Lightning", 3: "Earth", 4: "Dark", 5: "Light"
    }

    __eleicon = {
        0: '🔥', 1: '🌊', 2: '⚡️', 3: '⛰️', 4: '☀️', 5: '🌑'
    }
    __elecheck = []
    for k, v in __eletype.items():
        __elecheck.append(k)

    __val = []
    __key = []
    for k, v in __grade_value_multiplier.items():
        __key.append(k)
        __val.append(v)

    def __init__(self, name, tp, level, rarity, upgrades, star_crafted, bonus_stats):

        self._Item_name = name
        self._Item_type = tp
        self._Item_level = level
        self._Item_rarity = rarity
        self._Item_upgrades = upgrades
        self._Item_star_crafted = star_crafted

        # Calculate tier
        self._Item_tier = int(math.floor(self._Item_level / 10))

        # Generate durability when initialize new instance
        self._Item_durability[0] = self._Item_durability[1] = self.set_durability(self._Item_tier, self._Item_rarity)

        # These are the handlers for created instance.
        # Handler for name
        if (self._Item_name is None) or (self._Item_name == '') or (type(self._Item_name) is not str):
            self._Item_name = "Undefined"

        # Handler for level
        if (self._Item_level is None) or (self._Item_level < 1) or (type(self._Item_level) is not int):
            self._Item_level = 1

        # Handler for rarity
        is_valid_rarity = lambda a: 0 <= a <= 5
        if(self._Item_rarity is None) or (not is_valid_rarity(self._Item_rarity)) or (type(self._Item_rarity) is not int):
            self._Item_rarity = 0

        # Handler for grade
        # if (self._Item_grade[0] not in self.__key) or (type(self._Item_grade) is not list):
        self._Item_grade = self.generate_grade()
        # else:
        #     pass

        # Handler for upgrades
        if (self._Item_upgrades < 0) or (self._Item_upgrades is None) or (type(self._Item_upgrades) is not int):
            self._Item_upgrades = 0

        # Handler for elemental type
        # if self._Item_element_type not in self.__elecheck:
        self._Item_element_type = self.generate_elemental_type(list(self.__eletype)[-1])
        # else:
        #     pass

        # Handler for durability
        if ((self._Item_durability[0] > self._Item_durability[1]) or (self._Item_durability is None) or
                (self._Item_durability[1] < 1)):
            self._Item_durability = [1, 1]

        # Handler for mastery
        if ((self._Item_mastery[0] > self._Item_mastery[1]) or (type(self._Item_mastery) is not list) or
                (self._Item_mastery[1] < 1)):
            self._Item_mastery = [0, 100]

        # Setter and handler for bonus stats
        if self._Item_bonus_stats != 0:
            # Ignore the string value (stat name) when create new instance
            self._Item_bonus_stats = self.generate_bonus_stats(self._Item_rarity, self._Item_type)
        else:
            self._Item_bonus_stats = bonus_stats # NOTE : NO HANDLER FOR THIS ATTRIBUTE, THINGS CAN GO WRONG

    # THESE ARE THE FUNCTIONS USE TO GENERATE/SET VALUE WHEN CREATE NEW INSTANCE
    @staticmethod
    def generate_number(number_of_results) -> int:
        # Get seed
        seed = int(hashlib.sha256(os.urandom(32)).hexdigest(), 16)
        # Return number
        return np.random.default_rng(seed=seed).choice(number_of_results)

    @staticmethod
    def import_data(path):
        with open(path, 'r') as JsonReader:
            return js.load(JsonReader)

    @staticmethod
    def generate_elemental_type(number_of_elements) -> int:
        seed = int(hashlib.sha256(os.urandom(32)).hexdigest(), 16)
        return np.random.default_rng(seed=seed).choice(number_of_elements)

    def generate_bonus_stats(self, item_rarity: int, item_type: int) -> list[list[int, int, str]]:
        seed = int(hashlib.sha256(os.urandom(32)).hexdigest(), 16)
        rng = np.random.default_rng(seed=seed)
        type_switcher = {
            0: file_paths[0],
            1: file_paths[1],
            2: file_paths[2],
            3: file_paths[3]
        }
        # Import data from file
        data = import_data(type_switcher.get(item_type))
        stats_pool = data['bonus-stats'] # Get the current stats from file
        upper_threshold = stats_pool[-1]['id'] + 1 # Get count of all bonus stats in file
        # Get random number of bonus stats from rarity ( Ex : Rare -> from 2 to 3 bonus stats )
        number_of_bonus_stats = self.__number_of_bs.get(item_rarity)[np.random.randint(2)]
        # Generate a set of selected ids
        selected_id = rng.choice(upper_threshold, number_of_bonus_stats, replace=False)

        selected_bonus_stats = []
        for _ in selected_id:
            stat = next((s for s in stats_pool if s['id'] == _))
            if stat:
                stat_name = stat['name']
                value_range = stat['value_range']
                is_flat = stat['is_flat']
                rate = stat['rate']
                display_value = 0
                if is_flat:
                    display_value = generated_value = rng.integers(value_range[0], value_range[1]+1)
                    selected_bonus_stats.append([_, generated_value, display_value, stat_name])
                else:
                    generated_value = rng.integers(value_range[0], value_range[1] + 1)
                    display_value = np.round(generated_value / rate, decimals = 2)
                    selected_bonus_stats.append([_, generated_value, display_value, stat_name])

        return selected_bonus_stats

    def set_durability(self, tr: int, rr: int) -> int:
        return self.__dur_multiplier.get(rr)*(rr+1) + self.__dur_multiplier.get(rr)*tr

    def generate_grade(self) -> (int, float):
        grade_as_int = np.random.default_rng(seed=int(time.time())).choice(5)
        grade_multipler = self.__grade_value_multiplier.get(grade_as_int)
        return(
            grade_as_int,
            grade_multipler
        )

    # THESE FUNCTIONS'S PURPOSE IS TO GIVE OUT VALUE AS STRING OUTPUT
    def rarity_mapping(self, item_rarity: int) -> str:
        return self.__rarity_name.get(item_rarity)

    def grade_mapping(self, item_grade: int) -> str:
        return self.__grade_name.get(item_grade)

    def element_mapping(self, item_element_type: int) -> (str, str):
        return (
            self.__eletype.get(item_element_type),
            self.__eleicon.get(item_element_type)
        )

    def __getitem__(self):
        return {
            "name": str(self._Item_name),
            "level": str(self._Item_level),
            "rarity": int(self._Item_rarity),
            "grade": list(self._Item_grade),
            "upgrades": int(self._Item_upgrades),
            "star": int(self._Item_star_crafted),
            "element": int(self._Item_element_type),
            "durability": list(self._Item_durability),
            "mastery": list(self._Item_mastery),
            "base_stats": list(self._Item_base_stats),
            "bonus_stats": list(self._Item_bonus_stats),
            "unique": list(self._Item_unique),
            "refinements": list(self._Item_refinements)
        }


def import_data(file):
    with open(file, 'r') as JsonReader:
        data = js.load(JsonReader)
    return data