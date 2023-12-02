##### 선호도 기반 음식 추천 프로그램 ####

# ~12/1 File Storage Func 완성 // 일정 밀림. 
# memos 저장 기능도 같이 추가하기. 

## 일정 조금씩 밀림, 일정 나중에 수정하기. 
# 메뉴 추천 기능 시작, 카테고리 선택 완성 및 메모 저장 기능 진행하기.  
# 카테고리 선택: 음식을 추천받고자 하는 카테고리 선택. 
# 메모 저장: 추천된 음식에 코멘트 남기기. 

import file_adit0 as fa # 파일 입출력기능.
#import file_edit as fa
import add_menu
import del_menu

# 메뉴, 선호도 등 정보 가져오기 
menus = {} # 카테고리와 메뉴 저장. 
ratings = {} # 음식별 별점. 
fa.load_file("./menus.csv",menus,ratings)

#메모 가져오기 
memos = {} # 음식별 메모. 
memos = fa.load_file("./memos.csv",menus,ratings)

# 테스트 
print("menu",menus)
print("ratings",ratings)
print("momos",memos)
    
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
            