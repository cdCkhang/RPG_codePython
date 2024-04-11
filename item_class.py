class Item:
    _Item_name: str = ""
    _Item_rarity: int = 0  # Ex : 1 - Rare
    _Item_grade: dict = {0: 0}  # Ex : 1[grade] - 9[value] ==> Excellent : +9% base stats
    _Item_upgrades: int = 0
    _Item_star_crafted: int = 0
    _Item_element_type: int = 0
    _Item_durability: list = [0, 0]  # Ex : 30,30 ==> Dur : 30/50
    _Item_mastery: list = [0, 0]  # Ex : 40,100 ==> Mas : 40/100
    _Item_base_stats: list[dict] = [{0: 0}]  # Ex : 1[id] : 130[value] ==> Physical attack : +130
    _Item_bonus_stats: list[dict] = [{0: 0}]  # Ex : 4[id] : 40[value] ==> Physical armor penetration : +40
    _Item_unique: dict = {0: 0}
    _Item_refinements: list[list[int, int]] = [(0, 0), (0, 0)]
    # Ex : [(1,2),(2,3)] ==> Ref#1 with level 2, Ref#2 with level 3

    def __init__(self, name, rarity, grade, upgrades, star_crafted, element_type, durability, mastery,
                 base_stats, bonus_stats, unique, refinements):
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
    def number_to_rarity(_item_rarity: int) -> str:
        switcher = {
            0: "Basic",
            1: "Rare",
            2: "Epic",
            3: "Legendary",
            4: "Mythic",
            5: "Divine"
        }
        return switcher.get(_item_rarity, "nothing")

    def __str__(self):
        pass

    def __getitem__(self):
        return self._Item_name

    def __setitem__(self):
        return

    def getName(self):
        return self._Item_name

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
        }





