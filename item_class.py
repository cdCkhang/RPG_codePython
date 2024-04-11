class Item:
    _Item_name: str = ""
    _Item_rarity: int = 0  # Ex : 1 - Rare
    _Item_grade: dict = {0: 0}  # Ex : 1[grade] - 9[value] ==> Excellent : +9% base stats
    _Item_upgrades: int = 0
    _Item_star_crafted: int = 0
    _Item_element_type: int = 0
    _Item_durability: list = [0, 0]  # Ex : 30,30 ==> Dur : 30/50
    _Item_mastery: list = [0, 0]  # Ex : 40,100 ==> Mas : 40/100
    _Item_base_stats: list[list] = [(0, 0)]  # Ex : 1[id], 130[value] ==> Physical attack : +130
    _Item_bonus_stats: list[list] = [(0, 0)]  # Ex : 4[id], 40[value] ==> Physical armor penetration : +40
    _Item_unique: dict = {0: 0} # Ex : 1[id], 2[level/value] ==> Increase basic attack damage by %
    _Item_refinements: list[list[int, int]] = [(0, 0), (0, 0)] # Ex : [(1,2),(2,3)] ==> Ref#1 with level 2, Ref#2 with level 3

    def __init__(self, name, rarity, grade, upgrades, star_crafted, element_type, durability, mastery,
                 base_stats, bonus_stats, unique=None, refinements=None):
        self._Item_name = name
        self._Item_rarity = rarity
        self._Item_grade = grade
        self._Item_upgrades = upgrades
        self._Item_star_crafted = star_crafted
        self._Item_element_type = element_type
        self._Item_durability = durability
        self._Item_mastery = mastery
        self._Item_base_stats = base_stats
        self._Item_bonus_stats = bonus_stats
        self._Item_unique = unique
        self._Item_refinements = refinements

    @staticmethod
    def rarity_mapping(_item_rarity: int) -> (str, int):
        rarity_name = {
            0: "Basic",
            1: "Rare",
            2: "Epic",
            3: "Legendary",
            4: "Mythic",
            5: "Divine"
        }
        number_of_bs = {
            0: 1,
            1: [1, 2],
            2: [2, 3],
            3: [4, 5],
            4: 6,
            5: 6
        }
        return {
            rarity_name.get(_item_rarity, "Undefined"),
            number_of_bs.get(_item_rarity, 1)
        }

    @staticmethod
    def grade_mapping(_item_grade: int) -> (str, float):
        grade_name = {
            0: "Standard",
            1: "Fine",
            2: "Excellent",
            3: "Perfect",
            4: "Supreme",
        }
        grade_value_multiplier = {
            0: 1.0,   # No bonus
            1: 1.03,  # 3% base stats
            2: 1.06,  # 6% base stats
            3: 1.09,  # 9% base stats
            4: 1.12   # 12% base stats
        }
        return {
            grade_name.get(_item_grade, "Undefined"),
            grade_value_multiplier.get(_item_grade, 1.0)
        }

    @staticmethod
    def element_mapping(_item_element_type: int) -> (str, int):
        eletype = {
            0: "Fire",
            1: "Water",
            2: "Lightning",
            3: "Earth",
            4: "Dark",
            5: "Light"
        }
        return{
            eletype.get(_item_element_type, "None"),
            _item_element_type
        }

    def __getitem__(self):
        return {
            "name": self._Item_name,
            "rarity": self._Item_rarity,
            "grade": self._Item_grade,
            "upgrades": self._Item_upgrades,
            "star": (self._Item_star_crafted * '★'),
            "element": self._Item_element_type,
            "durability": self._Item_durability,
            "mastery": self._Item_mastery,
            "base_stats": self._Item_base_stats,
            "bonus_stats": self._Item_bonus_stats,
            "unique": self._Item_unique,
            "refinements": self._Item_refinements
        }

    @property
    def GetItemAttribute(self):
        return {
            "name": self._Item_name,
            "rarity": self._Item_rarity,
            "grade": self._Item_grade,
            "upgrades": self._Item_upgrades,
            "star": self._Item_star_crafted,
            "element": self._Item_element_type,
            "durability": self._Item_durability,
            "mastery": self._Item_mastery,
            "base_stats": self._Item_base_stats,
            "bonus_stats": self._Item_bonus_stats,
            "unique": self._Item_unique,
            "refinements": self._Item_refinements
        }

    def __setitem__(self):
        if self._Item_durability[0] > self._Item_durability[1]:
            self._Item_durability = [1, 1]
        if self._Item_mastery[0] > self._Item_mastery[1]:
            self._Item_mastery = [0, 100]