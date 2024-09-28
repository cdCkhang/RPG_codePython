class CONSTANTS_STATS:

    # ===============================================================================================
    #                         <<<<<     MODIFIERS, DICTIONARIES       >>>>>
    #             Constant values for calculation, output purpose. Can be used by all items.
    # ===============================================================================================
    # Base value
    # Attacks ( Offensive )
    Map_base_attacks = {
        0: 5,  # 0 - Physical,
        1: 8   # 1 - Magic
    }
    Base_element_attack = 6

    # Health and Armors ( Defensive )
    Base_health = 30
    Base_physical_armor = 5
    Base_magic_armor = 4
    Map_random_armor = {
        # 0 - Physical armor, 1 - Magic amor, 2 - Both
        0: [0], 1: [1], 2:[0,1]
    }
    # Single armor equipm. will have more base armor comparing to dual armors equipment
    Map_armor_base_multiplier = {
        # 0 - Physical armor, 1 - Magic amor, 2 - Both
        0: 1.8, 1: 1.6, 2: 1.0
    }

    # Masteries
    Rate_mastery = 100 # Standard divison number for mastery. Value range: 0 - 300
    # Upper and lower limit for mastery
    Min_mastery = 0
    Max_mastery = 300
    Universal_mastery_stack = 0.12  # +12% / mastery stack
    Offensive_mastery_multiplier = 0.0008 # +0.8% / mastery point
    # 0 - Single armor, 1 - Dual armor
    Defensive_master_multiplier = {
        0: [0.0015, 0.0012], # +0.15% health and +0.12% armor [single armor] per point
        1:[0.0008, 0.0006] # +0.08% for health and +0.06% armor [dual armor] per point
    }
    Hybrid_mastery_stack = 0.06
    Hybrid_mastery_multiplier = 0.0004

    # Upgrades, Stars
    Multiplier_uprades = 0.03 # +3% base stats value / Upgrade
    Multiplier_star = 0.1 # +10% bonus stats value / Star


    # Item types and attacks, for: string output
    Map_item_type = {
        0: "Physical",
        1: "Magic",
        2: "Defensive",
        3: "Hybrid"
    }
    Map_primary_attack = {
        0: "Physical", 1: "Magic"
    }


    # Rarity name dict, for: string output
    Map_rarity_name = {
        0: "Basic",
        1: "Rare",
        2: "Epic",
        3: "Legendary",
        4: "Mythic",
        5: "Divine"
    }

    # Rarity buff dict, for: get bonus stats buff based on rarities
    Map_rarity_buff_rate = {
        0: 0.0,  # Basic
        1: 0.0,  # Rare
        2: 0.0,  # Epic
        3: 0.15,  # Legendary
        4: 0.25,  # Mythic
        5: 0.4  # Divine
    }
    # Rarities dict, for: get number of bonus stats based on rarities
    Map_numberofbs = {
        0: [1, 2],  # Basic
        1: [2, 3],  # Rare
        2: [3, 4],  # Epic
        3: [4, 5],  # Legendary
        4: [5, 6],  # Mythic
        5: [6, 6]  # Divine
    }


    # Durability dict for: calculate dur based on rarity
    Map_durability = {
        0: 15,  # Basic
        1: 15,  # Rare
        2: 16,  # Epic
        3: 16,  # Legendary
        4: 17,  # Mythic
        5: 18   # Divine
    }

    # ??? What the literal fuck is this
    Map_tier_multiplier = {
        1: 5, 2: 5, 3: 1
    }


    # Base stats dict for: multipliers based on item's tier
    # Ranging from tier 0 (lv-1 to lv-10 ) to tier 14 (lv.141-150)
    Map_base_multiplier = {
        0: 4, 1: 5, 2: 6, 3: 7, 4: 8, 5: 9,
        6: 10, 7: 11, 8: 12, 9: 13, 10: 14,
        11: 15, 12: 16, 13: 17, 14: 18
    }
    Map_sub_multiplier = {
        0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7,
        6: 8, 7: 9, 8: 10, 9: 11, 10: 12,
        11: 13, 12: 14, 13: 15, 14: 16
    }

    # Grades dict for: string output + value multiplier
    Map_grade_name = {
        0: "Standard",
        1: "Fine",
        2: "Excellent",
        3: "Perfect",
        4: "Supreme"
    }

    Map_grade_value = {
        0: 0.0,  # Standard (+0%)
        1: 0.03,  # Fine (+3%)
        2: 0.06,  # Excellent (+6%)
        3: 0.09,  # Perfect (+9%)
        4: 0.12  # Supreme (+12%)
    }

    Map_element_name = {
        0: "Pyro",
        1: "Hydro",
        2: "Electro",
        3: "Geo",
        4: "Scoto",
        5: "Photon"
    }
    # ELement's icon use for output purpose
    Map_element_icon = {
        0: '🔥', 1: '🌊', 2: '⚡️',
        3: '⛰️', 4: '🌑', 5: '☀️'
    }
