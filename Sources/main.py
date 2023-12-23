##### 선호도 기반 음식 추천 프로그램 ####

import pandas as pd
import choice # 선택지
import random


# 정보 가져오기
data= pd.read_csv('menus.csv') 

# 정보 저장.  
menus = {} # {category1 : {menu1,menu2....}, category2 : {....}}
end_menu = {}
for index, row in data.iterrows():
    category = row['Category']
    menu = row['Menu']

    if category not in menus: # 새로운 카테고리 추가. 
        menus[category] = {}
    menus[category][menu] = row['Ratings']

ratings = {} # Menu : Ratings
for index, row in data.iterrows():
    menu = row['Menu']
    rating = row['Ratings']
    ratings[menu] = rating

memos = {} # Menu : Memo
for index, row in data.iterrows():
    menu = row['Menu']
    memo = row['Memo'] 
    memos[menu] = memo

 # 테스트
print("menus",menus)
print("ratings",ratings)
#print("memos",memos)

while True: 
    print(""" 
      1. 메뉴 추가 
      2. 메뉴 삭제 
      3. 메뉴 추천 
      4. 종료
      """)
    choice_todo = int(input("할 일을 선택해주세요. (1~4)"))

    if (choice_todo == 1):
        print(*menus.keys()) # 카테고리 보여주기 
        choice.add_menu(menus,ratings,memos)


    elif (choice_todo == 2): 
        print("메뉴를 삭제합니다. ")
        choice.del_menu(menus,ratings,memos)
        

    elif (choice_todo == 3 ):
        
        print(*menus.keys())
        while True:
            recommend_cate = input("메뉴를 추천받을 카테고리를 선택해 주세요.")
            if recommend_cate not in menus.keys():
                print("선택한 카테고리가 존재하지 않습니다. 다시 선택해 주세요. ")
            else:
                break


        # 카테고리의 끝까지만 추출해 사용할 필요. 
        # menus category의 카테고리별 마지막 값 찾기 
        end_menus = {} # 카테고리별 마지막 메뉴들 저장. 
        for category,menu in menus.items():
            print(menu)
            end_menus[category] = list(menu)[-1]

        print("end_menus",end_menus)


        recommend_ratings = {} # 정한 카테고리의 end menu까지만 저장하는 새로운 dict 생성. 
        for menu in ratings.keys():
            if menu == end_menus[recommend_cate]: 
                break  
            recommend_ratings[menu] = ratings[menu]
        print("recommend_ratings",recommend_ratings)


        def WeightedRandom(ratings):
            total_weight = sum(ratings.values()) # rating 총합
            rand_val = random.uniform(0,total_weight) # 0~ total weight 사이 무작위 실수 추출. 

            shuffled_rating = list(ratings.items()) 
            random.shuffle(shuffled_rating) # ratings를 랜덤으로 섞은 shuffled_rating 반환. 

            current_weight = 0 # 초기화 
            for menu,rating in shuffled_rating.items():
                current_weight += rating # 뒤로 갈수록 점점 확률이 높아짐, 자체 선호도가 높아도 추천 확률 높아짐. 
                if rand_val <= current_weight: # 누적 선호도가 랜덤 값보다 높아지는 순간 선택. 
                    return menu
                
        #WeightedRandom(ratings.values())  


    # 종료 및 파일에 반영
    elif (choice_todo == 4): 
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
            




# 완성헤야 하는 것. 
# Menu Recommendation (대주제)
# - Save Memo : 추천된 메뉴에 메모 남기기. 
# - Select category : 메뉴를 추천받을 카테고리 선정하기 
# - Save Preferences : 추천된 메뉴에 선호도를 남기고 
# 새로운 음식 추천에 반영될 수 있도록 하기 


# 완성한 것. (보완 필요)
# - Add Menu
# - Delete Menu
# - File Storage Function


# try - except 잘 쓰기 