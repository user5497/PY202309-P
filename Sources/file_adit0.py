# 파일 관리 기능들. 

# 카테고리별 마지막 값 저장용
end_menus= []
end_ratings =[]

def load_file(file_name,menus,ratings):
    lines = open(file_name,"r",encoding = "utf8").readlines()
    for line in lines:
        tokens = line.strip().split(",")
        #print("tokens",tokens) # 테스트

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
    print("end_menus",end_menus)
    print("end_ratings",end_ratings)

    
    if (file_name == "./menus.csv"):
        return menus,ratings
    elif (file_name == "./memos.csv"):
        return ratings




# memos 저장하기
# 카테고리별 end_value를 저장해서 반영하는 방법 구현 중. *********

def save_file(file_name,menus,ratings):
    write_fp = open(file_name,"w",encoding = "utf8")

    for category in menus.keys():
        line = [category]
    
        for food,rating in ratings.items(): 
            #print("food",food) # 음식 하나씩 나열
            line.append(food)
            line.append(rating)
            if (rating == end_ratings):
                line.append(rating) #여기서 같은 rating을 가지고 있어서 문제 발생. 
                line.append("\n")
            
        write_line = str(line).replace("'","").replace("[","").replace("]","").replace(" ","")
        write_fp.write(write_line + "\n")

    write_fp.close()
