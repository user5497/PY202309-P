# 파일 관리 기능들. 

# 카테고리별 마지막 값 저장용
end_menus= []
end_ratings =[]

def load_file(file_name,menus,ratings):
    lines = open(file_name,"r",encoding = "utf8").readlines()
    for line in lines:
        tokens = line.strip().split(",")
        print("tokens",tokens) # 테스트

        end_menus.append(tokens[-2])
        end_ratings.append(tokens[-1])

        food_list = [] # 편집 용이 
        for i in range(1,len(tokens)):
            try:
                ratings[tokens[2*i-1]] = tokens[2*i] # 음식별 별점 할당. 
                food_list.append(tokens[2*i-1])
            except IndexError: # 빈 값을 입력하려 하는 경우 제외 
                continue

            menus[tokens[0]] = (food_list)
    
    # 테스트 
    print(end_menus)
    print(end_ratings)
    print("메뉴를 정상적으로 불러왔습니다. ")




def save_file(file_name,menus,ratings):
    write_fp = open(file_name,"w",encoding = "utf8")

    for category in menus.keys():
        line = [category]
        
        # 카테고리별 end_value를 저장해서 반영하는 방법 구현 중. 
        for food,rating in ratings.items(): 
            print("food",food) # 음식 하나씩 나열

        write_line = str(line).replace("'","").replace("[","").replace("]","").replace(" ","")
        write_fp.write(write_line + "\n")

    write_fp.close()
