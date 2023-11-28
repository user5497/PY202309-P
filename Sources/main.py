##### 선호도 기반 음식 추천 프로그램 ####

# ~12/1 File Storage Func 완성 
# memos 저장 기능도 같이 추가하기. 

import file_adit as fa # 파일 입출력기능.
import add_menu
import del_menu

menus = {} # 카테고리와 메뉴 저장. 
meno = {} # 음식별 메모. 
ratings = {} # 음식별 별점. 


# 메뉴, 선호도 등 정보 가져오기 
fa.load_file("./menus.csv",menus,ratings)

# 메모 가져오기 
#fa.load_file("./memos.csv")

# 테스트 
#print("menu",menus)
#print("ratings",ratings)
    
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
        print("메뉴: ", *menus.keys()) # 카테고리 보여주기

        add_menu.add_m(menus,ratings)
    
    elif (choice == 2): 
        print("메뉴를 삭제합니다. ")
        print(*menus.keys())
        del_menu.del_m(menus,ratings)
        

    elif (choice == 3 ):
        pass

    elif (choice == 4): 
        # 종료 및 파일에 반영
        print("종료합니다. ")
        fa.save_file("./menus.csv",menus,ratings)
        break

    else: 
        print("잘못된 번호를 선택했습니다. 다시 입력해 주세요.")
        continue
            