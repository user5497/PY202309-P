##### 선호도 기반 음식 추천 프로그램 ####

import pandas as pd
import choice # 선택지별 기능



# 정보 가져오기
data= pd.read_csv('menus.csv') 
#print(data.to_string(index=False)) # 추가 인덱스 생성 제거 

# 카테고리 정보 저장
category = [] 
for cate in data.Category:
    if cate not in category:
        category.append(cate)
#print("cate",*category)



while True: 
    print(""" 
      1. 메뉴 추가 
      2. 메뉴 삭제 
      3. 메뉴 추천 
      4. 종료
      """)
    choice = int(input("할 일을 선택해주세요. (1~4)"))

    if (choice == 1):
        print("메뉴를 추가합니다.")
        print("메뉴: ", *category) # 카테고리 보여주기

        choice.add_menu(data,category)
    

    elif (choice == 2): 
        print("메뉴를 삭제합니다. ")
        print(*category)
        choice.del_menu(data)
        


    elif (choice == 3 ):
        pass



    elif (choice == 4): 
        # 종료 및 파일에 반영
        print("종료합니다. ")
        # 파일 반영
        break

    else: 
        print("잘못된 번호를 선택했습니다. 다시 입력해 주세요.")
        continue
            



# pandas 도입하고 내용 너무 간단해짐. 추가할 내용 생각해보기 
# 막 가장 많이 먹은 음식 그래프 표시나 별점 높은 순 시각화 이런 거 할 수 있나
# 오류처리 까먹지말기. (try - except)

# ~12/1 File Storage Func 완성 // 일정 밀림. 
# memos 저장 기능도 같이 추가하기. 

# 메뉴 추천 기능 시작, 카테고리 선택 완성 및 메모 저장 기능 -진행-하기. 
# 카테고리 선택: 음식을 추천받고자 하는 카테고리 선택. 
# 메모 저장: 추천된 음식에 코멘트 남기기. 