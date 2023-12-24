import random

# 메뉴 추가 
def add_menu(menus,memos): 
    while True: # 존재하지 않는 카테고리를 입력받는 경우 차단. 
        add_cate = input("메뉴 추가를 원하는 카테고리를 선택해 주세요. ")
        if add_cate not in menus.keys(): 
            print("입력한 카테고리가 존재하지 않습니다. ") 
        else:
            break

    add_menu = input("추가를 원하는 메뉴를 입력해 주세요. ")

    while True: # 정수만 입력 
        try:
            add_rate = int(input("추가한 메뉴에 별점을 남겨 주세요. "))
            break
        except ValueError: 
            print("숫자를 입력해 주세요. ")
    

    input_memo = input("메모를 남기시겠습니까? (y/n)")
    memo = " " # 메모를 남기지 않는 경우
    if (input_memo == 'y'):
        memo = input("메모를 입력해주세요. ")

    menus[add_cate][add_menu] =  add_rate
    memos[add_menu] = memo
    print("메뉴 추가가 완료되었습니다. ")
    #print("menus",menus)
    #print("memos",memos)


# 메뉴 삭제
def del_menu(menus,memos):
    while True: # 존재하지 않는 카테고리를 입력받는 경우 차단. 
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

    del menus[del_cate][del_menu]
    del memos[del_menu]
    print("삭제가 완료되었습니다. ")

    print("menus",menus[del_cate])
    print("memos",memos)


# 메뉴 추천.
def RecommendMenu(recommend_menus):
    total_weight = sum(recommend_menus.values()) # rating 총합
    rand_val = random.uniform(0,total_weight) # 0~ total weight 사이 무작위 실수 추출. 

    shuffled_rating = list(recommend_menus.items()) 
    random.shuffle(shuffled_rating) # ratings를 랜덤으로 섞은 shuffled_rating 반환. 
    shuffled_rating = dict(shuffled_rating)
    # print("shuffled_rating",shuffled_rating) # 테스트 

    current_weight = 0 # 초기화 
    for menu,rating in shuffled_rating.items():
        current_weight += rating # 뒤로 갈수록 점점 확률이 높아짐, 자체 선호도가 높아도 추천 확률 높아짐. 
        if rand_val <= current_weight: # 누적 선호도가 랜덤 값보다 높아지는 순간 선택. 
            return menu
                
        