
# choice == 1 메뉴 추가
def add_menu(data,category): 
    print("cate",category)
    print("data",data)
    
    
    while True: # 알맞은 카테고리만 입력받기 
        add_cate = input("메뉴 추가를 원하는 카테고리를 선택해 주세요. ")
        if add_cate not in category:
            print("입력한 카테고리가 존재하지 않습니다. ") 
            continue
        else:
            break
    
    # 메뉴 추가 
    add_menu = input("추가를 원하는 메뉴를 입력해 주세요. ")
    data.loc[data['Category'] == add_cate,'Menu'] = add_menu 

    # 별점 추가 
    while (1):
        add_rat = input("추가한 메뉴에 별점을 남겨 주세요. ")
        if (type(add_rat) != int): # 숫자만 입력받기 
            print("숫자를 입력해주세요. ")
        else:
            break
    data.loc[data['Menu'] == add_menu,'Ratings'] = add_rat

    # 메모 추가 
    input_memo = input("메모를 남기시겠습니까? (y/n)")
    input_memo = input_memo.lower() 
    if (input_memo == 'y'): 
        memo = input("남길 메모를 입력해주세요: ")
        data.loc[data['Menu'] == add_menu,'Memo'] = memo
    elif (input_memo != 'n'):
        print("잘못된 선택입니다. 메모를 남기지 않습니다. ")
        

    print("메뉴 추가가 완료되었습니다. ")
    print(data.loc[data['Menu']==add_menu])




# choice == 2 메뉴 삭제
def del_menu(data):
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

