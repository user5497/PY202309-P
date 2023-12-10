##### 선호도 기반 음식 추천 프로그램 ####

import pandas as pd
import choice


# 정보 가져오기
data= pd.read_csv('menus.csv') 

# 정보 저장.  
menus = {}
for index, row in data.iterrows():
    category = row['Category']
    menu = row['Menu']
    if category not in menus:
        menus[category] = set()
    menus[category].add(menu)

ratings = {}
for index, row in data.iterrows():
    menu = row['Menu']
    rating = row['Ratings']
    ratings[menu] = rating

memos = {}
for index, row in data.iterrows():
    menu = row['Menu']
    memo = row['Memo'] 
    memos[menu] = memo






while True: 
    print(""" 
      1. 메뉴 추가 
      2. 메뉴 삭제 
      3. 메뉴 추천 
      4. 종료
      """)
    choice_todo = int(input("할 일을 선택해주세요. (1~4)"))

    if (choice_todo == 1):
        print("메뉴를 추가합니다.")
        # 카테고리 보여주기 
        choice.add_menu(menus,ratings,memos)


    elif (choice_todo == 2): 
        print("메뉴를 삭제합니다. ")
        choice.del_menu(menus,ratings,memos)
        


    elif (choice_todo == 3 ):
        pass


    # 종료 및 파일에 반영
    elif (choice_todo == 4): 

         # 테스트
        #print("menus",menus)
        #print("ratings",ratings)
        #print("memos",memos)

        print("종료합니다. ")

        # menus, ratings, memos를 DataFrame으로 변환
        menus_df = pd.DataFrame(list(menus.items()), columns=['Category', 'Menu']).explode('Menu').reset_index(drop=True)
        ratings_df = pd.DataFrame(list(ratings.items()), columns=['Menu', 'Ratings'])
        memos_df = pd.DataFrame(list(memos.items()), columns=['Menu', 'Memo'])

        # menus, ratings, memos를 병합
        result_df = pd.merge(menus_df, ratings_df, on='Menu')
        result_df = pd.merge(result_df, memos_df, on='Menu')

        # 결과를 csv 파일로 저장
        result_df.to_csv('menus.csv', index=False)
        break

    else: 
        print("잘못된 번호를 선택했습니다. 다시 입력해 주세요.")
        continue
            







# 메뉴 추천 기능 시작, 카테고리 선택 완성 및 메모 저장 기능 -진행-하기. 
# 카테고리 선택: 음식을 추천받고자 하는 카테고리 선택. 
# 메모 저장: 추천된 음식에 코멘트 남기기. 

