##### 선호도 기반 음식 추천 프로그램 ####
# 전반적 변수 가독성 개선 필요. 


import pandas as pd
import choice # 선택지

# 정보 가져오기
data= pd.read_csv('menus.csv') 

# 정보 저장.  
menus = {} 
for index, row in data.iterrows():
    category = row['Category']
    menu = row['Menu']
    if category not in menus: # 새로운 카테고리 추가. 
        menus[category] = {}
    menus[category][menu] = row['Ratings']

memos = {} 
for index, row in data.iterrows():
    menu = row['Menu']
    memo = row['Memo'] 
    memos[menu] = memo

 # 테스트
#print("menus",menus)
#print("memos",memos)


while True: 
    print(""" 
      1. 메뉴 추가 
      2. 메뉴 삭제 
      3. 메뉴 추천 
      4. 종료
      """)
      
    while True: # 정수만 입력 
        try:
            choice_todo = int(input("할 일을 선택해주세요. (1~4)"))
            break
        except ValueError: 
            print("숫자를 입력해 주세요. ")
    

    if (choice_todo == 1): # 메뉴 추가. 
        print(*menus.keys()) # 가독성. 
        choice.add_menu(menus,memos)


    elif (choice_todo == 2): 
        print("메뉴를 삭제합니다. ")
        print(*menus.keys())
        choice.del_menu(menus,memos)
        

    elif (choice_todo == 3 ):
        print(*menus.keys()) 
        while True: # 존재하지 않는 카테고리를 입력받는 경우 차단. 
            while True: 
                recommend_cate = input("메뉴를 추천받을 카테고리를 선택해 주세요.")
                if recommend_cate not in menus.keys():
                    print("선택한 카테고리가 존재하지 않습니다. 다시 선택해 주세요. ")
                else:
                    break

            # 선택한 카테고리의 정보만 저장하는 recommned_menus 생성.
            recommend_menus = menus.get(recommend_cate) 
            recommend_menu = choice.RecommendMenu(recommend_menus)
            print(f"{recommend_menu}(을/를) 추천합니다.")  
            print("이 메뉴에 남긴 메모는", memos[recommend_menu],"입니다.")


            while True: # 정수만 입력 
                try:
                    new_rate = int(input(f"{recommend_menu}의 별점을 남겨 주세요."))
                    break
                except ValueError: 
                    print("숫자를 입력해 주세요. ")
  
            input_memo = input("메모를 남기시겠습니까? (y/n)")
            new_memo = " "
            if (input_memo == 'y'):
                new_memo = input("메모를 입력해주세요. ")

            menus[recommend_cate][recommend_menu] = new_rate
            memos[recommend_menu] = new_memo
            

            again = input("다시 추천받으시겠습니까? (y/n)").lower()
            if (again == 'y'):
                continue
            else: # 잘못된 입력도 추천 종료로 간주. 
                print("추천을 종료합니다. ")
                break


    # 종료 및 파일에 반영
    elif (choice_todo == 4): 
        print("종료합니다. ")

        # menus, memos를 DataFrame으로 변환
        menus_df = pd.DataFrame([(cate, menu, rate) for cate, menu_rates in menus.items() for menu, rate in menu_rates.items()]\
                                , columns=['Category', 'Menu', 'Ratings'])
        memos_df = pd.DataFrame(list(memos.items()), columns=['Menu', 'Memo'])

        # menus, memos를 병합
        result_df = pd.merge(menus_df, memos_df, on='Menu')

        # 결과를 csv 파일로 저장
        result_df.to_csv('menus.csv', index=False)
        break

    else: 
        print("잘못된 번호를 선택했습니다. 다시 입력해 주세요.")
        continue

    