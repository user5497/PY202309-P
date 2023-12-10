
# 1번 메뉴 추가 
def add_menu(menus,ratings,memos): 
    while True: # 알맞은 카테고리만 입력받기 
        add_cate = input("메뉴 추가를 원하는 카테고리를 선택해 주세요. ")
        if add_cate not in menus.keys():
            print("입력한 카테고리가 존재하지 않습니다. ") 
        else:
            break

    add_menu = input("추가를 원하는 메뉴를 입력해 주세요. ")
    add_rat = input("추가한 메뉴에 별점을 남겨 주세요. ")
    input_memo = input("메모를 남기시겠습니까? (y/n)")
    memo = " "
    if (input_memo == 'y'):
        memo = input("메모를 입력해주세요. ")

    menus[add_cate].add(add_menu) 
    ratings[add_menu] = add_rat
    memos[add_menu] = memo
    print("메뉴 추가가 완료되었습니다. ")

    #print("menu", menus[add_cate])
    #print("ratings",ratings)



# 2번 메뉴 삭제
def del_menu(menus,ratings,memos):
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

    #print("menus",menus[del_cate])
    #print("ratings",ratings)