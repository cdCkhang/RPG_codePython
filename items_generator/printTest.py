# Main branch

from item_class import Item as classitem


def createNewItem() -> classitem:
    i_name = "Cursed Broken Sword from the Abyss"
    i_type = 0
    i_level = 30
    i_rarity = 1
    i_upgrades = 0
    i_mastery = 0
    i_star_crafted = 0
    generateditem = classitem(i_name, i_type, i_level, i_rarity, i_upgrades, i_mastery ,i_star_crafted)
    return generateditem


def GetAttributes(instance: classitem):
    name = instance.__getitem__()['name']
    level = str(instance.__getitem__()['level'])
    tier = instance.__getitem__()['tier']
    dur = instance.__getitem__()['durability']
    cur_dur, max_dur = dur[0], dur[1]
    element_id = instance.__getitem__()['element']
    element_name, element_icon = instance.s_element_mapping(element_id)
    rarity_id = instance.__getitem__()['rarity']
    rarity = instance.s_rarity_mapping(rarity_id)
    mastery = instance.__getitem__()['mastery']
    cur_mas = mastery[0]
    max_mas = mastery[1]
    stack_mas = mastery[2]
    rgrade = instance.__getitem__()['grade']
    grade = instance.s_grade_mapping(rgrade[0])
    grade_value = str(int(rgrade[1] * 100))
    upgrade = str(instance.__getitem__()['upgrades'])
    stars = str(instance.__getitem__()['star'])
    base_stats = instance.__getitem__()['base_stats']
    bonus_stats = instance.__getitem__()['bonus_stats']

    return (
        name, level, tier, cur_dur, max_dur, element_name, element_icon, rarity, cur_mas, max_mas, stack_mas, grade,
        grade_value, upgrade, stars,base_stats, bonus_stats
        # Use this for an easier life. Dont guess what is the n-th element in a list.
    )


def showItemInfo(instance: classitem):
    (i_name, i_level, i_tier, d1, d2, ele_name, ele_icon, i_rarity, i_curmas, i_maxmas, i_masstack, g_name, g_val,
     i_upgrade, i_stars, i_base, i_bonus) = GetAttributes(instance)
    n = 80
    print('=' * 33, "Item Details", '=' * 33)
    print(f"<{int(i_stars) * '★'}> [{i_rarity}][Lv.{i_level}][{ele_icon}] / {i_name} / (+{i_upgrade})")
    print('-' * n)
    print(f"Type: Tier {i_tier} - [{ele_name}] Mage class weapon")
    print(f"Grade: {g_name} (+{g_val}% base stats)")
    print(f"Mastery: {i_curmas}/{i_maxmas}[{i_masstack}]")
    print(f"Durability: {d1}/{d2}")
    print('-' * n)
    print('Base stats:')
    for i in i_base:
        print(f"    <+> {str(i[0])}: +{str(i[1])}")
    print('-' * n)
    print('Bonus stats:')
    for i in i_bonus:
        print(f"    [*] {str(i[3])}: +{str(i[1])}")


def main():
    newitem = createNewItem()
    showItemInfo(newitem)

if __name__ == '__main__':
    main()
