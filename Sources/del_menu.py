def del_m(menus,ratings):
    while True: # 카테고리 존재하지 않는 경우 삭제. 
        del_cate = input("삭제를 원하는 메뉴가 있는 카테고리를 선택해 주세요. ")
        if del_cate not in menus.keys():
            print("선택한 카테고리가 존재하지 않습니다. 다시 선택해 주세요. ")
            continue
        else:
            break

    print(*menus[del_cate])
    while True:
        del_menu = input("삭제를 원하는 메뉴를 선택해 주세요. ")
        if del_menu not in menus[del_cate]:
            print("해당 카테고리에 존재하지 않는 음식입니다. ")
            continue
        else:
            break

    menus[del_cate].remove(del_menu)
    del ratings[del_menu]
    print("삭제가 완료되었습니다. ")

    print("menus",menus[del_cate])
    print("ratings",ratings)

