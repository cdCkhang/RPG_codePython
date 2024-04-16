from item_class import Item as CLASS_ITEM

if __name__ == '__main__':
    # name, tp, level, rarity, upgrades, star_crafted, bonus_stats
    newItem = CLASS_ITEM("Staff of Doom", 1, 20, 4, 10, 4, 0)
    info_name = newItem.__getitem__()['name']
    info_level = newItem.__getitem__()['level']
    ele = newItem.__getitem__()['element']
    info_rarity = CLASS_ITEM.rarity_mapping(newItem, newItem.__getitem__()['rarity'])
    info_grade = newItem.__getitem__()['grade']
    grade_name = str(CLASS_ITEM.grade_mapping(newItem, info_grade[0]))
    grade_value = str(int((info_grade[1] - 1.0) * 100))
    info_upgrade = str(newItem.__getitem__()['upgrades'])
    info_stars = str(newItem.__getitem__()['star'])
    info_element, icon = CLASS_ITEM.element_mapping(newItem, ele)
    print('=' * 60)
    print('<<'+info_stars + '-Star>> (' + icon + ') ['+info_rarity+'] ' + info_name + ' || Lv.' + info_level + ' (+' + info_upgrade + ') ')
    print('-' * 60)
    print("Item's grade : " + grade_name + " [+" + grade_value + "% base stats]")
    print('-' * 60)
    for i in newItem.__getitem__()['bonus_stats']:
        print('- '+str(i[3]) + ': +'+str(i[1]) + '[' + str(i[2])+']')
    print('=' * 60)
