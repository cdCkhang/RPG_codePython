import os
import math
import hashlib
import numpy as np
import random

from utils.custom_hasher import hashing as customhash
from utils.Constants import CONSTANTS_STATS
from utils.JsonResourceHandler import file_paths
from utils.JsonResourceHandler import JsonResourceHandler

type_switcher = {
    0: file_paths[0],  # Physical
    1: file_paths[1],  # Magic
    2: file_paths[2],  # Defensive
    3: file_paths[3]   # Hybrid
}


class Item:
    # Attributes of an item
    _Item_name: str = ""
    _Item_type: int = 0
    _Item_rarity: int = 0
    _Item_element_type: int = -1
    _Item_level: int = 0
    _Item_tier: int = 0
    _Item_grade: list[int, float] = [0, 0]    # [1-id, 1.03-value] ==> Grade: Fine [+3% base stats]
    _Item_upgrades: int = 0
    _Item_star_crafted: int = 0
    _Item_durability: list = [-1, -1]# [30-remain, 50-max] ==> Dur: 30/50
    _Item_mastery: list[int, int, int] = [0,0,0]    # [245] ==> Mas: 45/100[2]
    _Item_base_stats: list[list[str, int]] = [(0, 0)]
    # ["stat_name", 130 - value] == > Physical attack: +13
    _Item_bonus_stats: list[list[int, int, str]] = [(0, 0, "")]
    # [0-id, 40-value, "stats_name"] ==> Physical attack: +40
    _Item_SA: list[int, int, str, int] or list[str] = ["", 0, 0, 0] or ["None"]
    _Item_REF: list[list[int, int, str]] = [(0, 0, ""),(0, 0, "")]  # [(1,2),(2,3)] ==> Ref id#1 lvl 2, Ref id#2 lvl 3

    # Independent variables.
    __type_name = CONSTANTS_STATS.Map_item_type
    __rarity_name = CONSTANTS_STATS.Map_rarity_name
    __rarity_value = CONSTANTS_STATS.Map_rarity_buff_rate
    __masrate = CONSTANTS_STATS.Rate_mastery
    __masmax = CONSTANTS_STATS.Max_mastery
    __masmin = CONSTANTS_STATS.Min_mastery
    __base_ele_atk = CONSTANTS_STATS.Base_element_attack
    __number_of_bs = CONSTANTS_STATS.Map_numberofbs
    __base_multiplier = CONSTANTS_STATS.Map_base_multiplier
    __sub_multiplier = CONSTANTS_STATS.Map_sub_multiplier
    __upgrade_multiplier = CONSTANTS_STATS.Multiplier_uprades
    __grade_name = CONSTANTS_STATS.Map_grade_name
    __grade_value = CONSTANTS_STATS.Map_grade_value
    __star_multiplier = CONSTANTS_STATS.Multiplier_star
    __dur_multiplier = CONSTANTS_STATS.Map_durability
    __eletype = CONSTANTS_STATS.Map_element_name
    __eleicon = CONSTANTS_STATS.Map_element_icon

    # Stats with multi types
    __special_stat_id = [22, 23, 24]

    def __init__(self, name="", itype=0, level=10, rarity=0, number_of_upgrades=0, mastery_point=0, star_crafted=0):
        # Get bonus stats from file by item's type
        file_content = JsonResourceHandler.import_data(str(type_switcher.get(self._Item_type)))
        self.Bonus_stats_data = file_content['bonus-stats']

        # Depenedent variable
        self.__base_atk = CONSTANTS_STATS.Map_base_attacks.get(self._Item_type)

        # Checking valid value when init new instance
        valid_rarity = self.__rarity_name.keys()
        valid_grade = self.__grade_name.keys()
        valid_element = self.__eletype.keys()

        self._Item_name = name
        if (self._Item_name == '') | (type(self._Item_name) is not str):
            self._Item_name = "?Undefined"

        self._Item_type = itype

        self._Item_level = level
        if (self._Item_level is None) | (self._Item_level < 1) | (type(self._Item_level) is not int):
            self._Item_level = 10

        self._Item_tier = Item.caculate_tier(self._Item_level)

        self._Item_rarity = rarity
        if (self._Item_rarity is None) | (self._Item_rarity not in valid_rarity) | (type(self._Item_rarity) is not int):
            self._Item_rarity = 1

        if (mastery_point > self.__masmax) | (mastery_point < self.__masmin):
            self._Item_mastery = [0, 100, 0]
        else:
            self._Item_mastery = self.calculate_mastery(mastery_point)

        self._Item_upgrades = number_of_upgrades
        if (self._Item_upgrades < 0) | (self._Item_upgrades is None) | (type(self._Item_upgrades) is not int):
            self._Item_upgrades = 0

        self._Item_star_crafted = star_crafted

        if self._Item_grade[0] not in valid_grade:
            self._Item_grade[0] = self.generate_grade()

        if (self._Item_durability[0] < 0) | (self._Item_durability[1] < 0) | (self._Item_durability[1] <
                                                                              self._Item_durability[0]):
            self._Item_durability[0] = self._Item_durability[1] = self.calculate_durability(self._Item_tier,
                                                                                            self._Item_rarity)

        if self._Item_element_type not in valid_element:
            self._Item_element_type = self.generate_elemental_type(list(self.__eletype)[-1] + 1)

        self._Item_base_stats = self.generate_base_stats(self.__base_atk, self.__base_ele_atk, self._Item_tier,
                                                         self._Item_level)
        self._Item_bonus_stats = self.generate_bonus_stats(self._Item_rarity)

        if self._Item_rarity > 2:
            self._Item_SA = [0,3,"Master-crafted","Increase all skills level by 3 levels"]
        else:
            self._Item_SA = ["None"]

        # Item unique id.
        self.ID = self.__hash__() * customhash.getmilisec()
        print(self.ID)


    # FUNCTIONS USE TO GENERATE/SET VALUE WHEN CREATE NEW INSTANCE
    @classmethod
    def generate_seed(cls) -> int:
        return int(hashlib.sha256(os.urandom(32)).hexdigest(), 16)

    @classmethod
    def generate_a_number(cls, lthreshold=1, uthreshold=1) -> int:
        random.seed(Item.generate_seed())
        return np.random.randint(lthreshold, uthreshold, dtype=int)

    @staticmethod
    def caculate_tier(lvl: int) -> int:
        return int(math.floor(lvl / 10))

    def calculate_mastery(self,total_mas: int) -> list[int, int, int]:
        mastery = list()
        stack = int(math.floor(total_mas / self.__masrate))
        current = int(round(total_mas % self.__masrate))
        mastery.extend([current, self.__masrate, stack])
        return mastery

    def calculate_durability(self, tr: int, rr: int) -> int:
        return self.__dur_multiplier.get(rr) * (rr + 1) + self.__dur_multiplier.get(rr) * tr

    def generate_grade(self) -> list[int, float]:
        grade = list()
        grade_as_int = Item.generate_a_number(0, 5)
        grade_multipler = self.__grade_value[grade_as_int]
        grade.extend([grade_as_int, grade_multipler])
        return grade

    @staticmethod
    def generate_elemental_type(number_of_elements) -> int:
        return Item.generate_a_number(0, number_of_elements)

    def calculate_base_modified_value(self, value: int) -> int:
        upgrade_multiplier = self._Item_upgrades * self.__upgrade_multiplier
        total_multiplier = 1 + upgrade_multiplier + self._Item_grade[1]
        return int(round(value * total_multiplier))

    def generate_base_stats(self, base_atk: int, base_ele_atk: int, tier: int, level: int) -> list[list[str, int]]:
        # Formula : (tier+1) * base * tier's multiplier + levels with
        nmod_primary_atk = (tier + 1) * base_atk * self.__base_multiplier.get(self._Item_tier) + (level - tier * 10) * base_atk * 0.5
        nmod_element_atk = (tier + 1) * base_ele_atk * self.__sub_multiplier.get(self._Item_tier) + (level - tier * 10) * base_ele_atk * 0.5
        primary_atk = self.calculate_base_modified_value(nmod_primary_atk)
        element_atk = self.calculate_base_modified_value(nmod_element_atk)
        base_atk_label = self.__type_name.get(self._Item_type) + " attack"
        ele_atk_label = self.__eletype.get(self._Item_element_type) + " elemental attack"
        base_stats = list()
        base_stats.append([base_atk_label, primary_atk])
        base_stats.append([ele_atk_label, element_atk])
        return base_stats

    def calculate_bonus_modified_value(self, value: int) -> int:
        total_modifiers_rate = (1 + self.__rarity_value.get(self._Item_rarity) +
                                (self._Item_star_crafted * self.__star_multiplier))
        return int(round(value * total_modifiers_rate))

    def generate_bonus_stats(self, item_rarity: int) -> list[list[int, int, str]]:
        rng = np.random.default_rng(seed=Item.generate_seed())
        # Get stats data
        data = self.Bonus_stats_data
        # Return number of stats
        upper_threshold = data[-1]['id'] + 1
        # Get random no of stats lines
        number_of_bonus_stats = self.__number_of_bs.get(item_rarity)[np.random.randint(2)]
        # Generate random stat ids
        generated_id = rng.choice(upper_threshold, number_of_bonus_stats, replace=False)
        selected_id = list(generated_id)
        selected_id.sort()
        # Remove any special ids in the selected list of ids
        special_stat = [sid for sid in selected_id if sid in self.__special_stat_id]
        selected_id = [sid for sid in selected_id if sid not in self.__special_stat_id]

        selected_bonus_stats = []
        for _ in selected_id:
            stat = next((s for s in data if s['id'] == _))
            if stat:
                stat_name = stat['name']
                value_range = stat['value_range']
                rate = stat['rate']
                display_value = generated_value = rng.integers(value_range[0], value_range[1] + 1)
                caculated_value = self.calculate_bonus_modified_value(generated_value)
                selected_bonus_stats.append([_, caculated_value, display_value, stat_name])

        return selected_bonus_stats

    # THESE FUNCTIONS ARE USED TO GIVE OUTPUT AS STRINGS
    def s_rarity_mapping(self, item_rarity: int) -> str:
        return self.__rarity_name.get(item_rarity)

    def s_grade_mapping(self, item_grade: int) -> str:
        return self.__grade_name.get(item_grade)

    def s_element_mapping(self, item_element_type: int) -> list[str, str]:
        element_info = list()
        element_info.append(self.__eletype.get(item_element_type))
        element_info.append(self.__eleicon.get(item_element_type))
        return element_info

    # 1st - level, 2 - type, 3 - name, 4 - desc
    @staticmethod
    def s_speical_attribute(special_attr: list[int, int, str, str]) -> list[str,str,str]:
        formatted = []
        if special_attr[0] == 0:
            sa_type = "Active"
        else:
            sa_type = "Passive"
        level = str(special_attr[1])
        name = special_attr[2]
        desc = special_attr[3]
        formatted.extend([sa_type, level, name, desc])
        return formatted

    def __getitem__(self):
        return {
            "name": str(self._Item_name),
            "level": str(self._Item_level),
            "tier": str(self._Item_tier),
            "rarity": int(self._Item_rarity),
            "grade": list(self._Item_grade),
            "upgrades": int(self._Item_upgrades),
            "star": int(self._Item_star_crafted),
            "element": int(self._Item_element_type),
            "durability": list(self._Item_durability),
            "mastery": list(self._Item_mastery),
            "base_stats": list(self._Item_base_stats),
            "bonus_stats": list(self._Item_bonus_stats),
            "special_attribute": list(self._Item_SA),
            "refinements": list(self._Item_REF)
        }
