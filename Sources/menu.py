##### 선호도 기반 음식 추천 프로그램 ####

# menu editing func
# 17일까지 : add menu 완성 & delete menu 진행하기. 



menu = {} # 카테고리와 메뉴 저장. 
meno = {} # 음식별 메모.
ratings = {} # 음식별 별점. 

# load data
lines = open("./menus.csv","r",encoding = "utf8").readlines()
for line in lines:
    tokens = line.strip().split(",")
    for i in range(1,len(tokens)-2,2):
        ratings[tokens[i]] = tokens[i+1] # 음식별 별점 할당. 
    menu[tokens[0]] = ratings
    

# 테스트
#print("menu",menu)
#print("ratings",ratings)



# 선택지 제공(메뉴 추가, 메뉴 삭제, 메뉴 추천) // 완료 시 파일 저장 기능

while True: 
    print(""" 
      1. 메뉴 추가 
      2. 메뉴 삭제 
      3. 메뉴 추천 
      """)
    choice = int(input("할 일을 선택해주세요. (1~3)"))

    if (choice == 1):
        print("메뉴를 추가합니다.")
        print("메뉴", *menu.keys())
        add_cate = input("메뉴 추가를 원하는 카테고리를 선택해 주세요. ")
        
        

        
        
  