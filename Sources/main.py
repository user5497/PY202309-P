##### 선호도 기반 음식 추천 프로그램 ####

# menu editing func/ File Storage func 
# 22일까지 기능 함수화 및 파일 분리 기능 구현하기. 

import file_adit as fa # 파일 입출력기능.
import choice # 각 선택지에 대한 기능들.

menu = {} # 카테고리와 메뉴 저장. 
meno = {} # 음식별 메모.
ratings = {} # 음식별 별점. 


# 메뉴, 선호도 등 정보 가져오기 
fa.load_file(ratings,menu)
print("menu",menu)
print("ratings",ratings)
    
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
        print("메뉴: ", *menu.keys()) # 카테고리 보여주기

        choice.add_menu(menu,ratings)
       
        #print("menu", menu)
        #print("ratings",ratings)
    
    elif (choice == 2): 
        print("메뉴를 삭제합니다. ")

        print(*menu.keys())
        choice.del_menu()
        

    elif (choice == 3 ):
        pass

    elif (choice == 4): 
        # 종료 및 파일에 반영
        print("종료합니다. ")
        fa.save_file(menu,ratings)
        break

    else: 
        print("잘못된 번호를 선택했습니다. 다시 입력해 주세요.")
        continue
            