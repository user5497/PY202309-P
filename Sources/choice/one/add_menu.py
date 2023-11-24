def add(menu,ratings): 
    while True: # 알맞은 카테고리만 입력받기 
        add_cate = input("메뉴 추가를 원하는 카테고리를 선택해 주세요. ")
        if add_cate not in menu.keys():
            print("입력한 카테고리가 존재하지 않습니다. ") 
        else:
            break
        
    add_menu = input("추가를 원하는 메뉴를 입력해 주세요. ")
    add_rat = input("추가한 메뉴에 별점을 남겨 주세요. ")
        
    menu[add_cate].append(add_menu) 
    ratings[add_menu] = add_rat
    print("메뉴 추가가 완료되었습니다. ")

