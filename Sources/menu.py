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
    # print(tokens)
    food_list = [] # 차후 편집을 위해 list 저장. 
    for i in range(1,len(tokens)):
        try:
            ratings[tokens[2*i-1]] = tokens[2*i] # 음식별 별점 할당. 
            food_list.append(tokens[2*i-1])
        except IndexError: # 빈 값을 입력하려 하는 경우 제외 
            continue
        menu[tokens[0]] = (food_list)
    
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
        print("메뉴: ", *menu.keys()) # 카테고리 보여주기

        while True: # 알맞은 카테고리만 입력받기 
            add_cate = input("메뉴 추가를 원하는 카테고리를 선택해 주세요. ")
            if add_cate not in menu.keys():
                print("입력한 카테고리가 존재하지 않습니다. ") 
            else:
                break
        
        add_menu = input("추가를 원하는 메뉴를 입력해 주세요. ")
        add_rat = input("추가한 메뉴에 별점을 남겨 주세요. ")
        
        menu[add_cate].append(add_menu) 
        ratings[add_menu] = add_rat
        print("메뉴 추가가 완료되었습니다. ")
       
        #print("menu", menu)
        #print("ratings",ratings)
    
    elif (choice == 2): 
        print("메뉴를 삭제합니다. ")

        del_cat = input("삭제를 원하는 메뉴가 있는 카테고리를 선택해 주세요. ")
        del_menu = input("삭제를 원하는 메뉴를 선택해 주세요. ")

        