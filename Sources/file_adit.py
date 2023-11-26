# 파일 관리 기능들. 

def load_file(menus,ratings): 
    lines = open("./menus.csv","r",encoding = "utf8").readlines()
    for line in lines:
        tokens = line.strip().split(",")
        # print(tokens)
        food_list = [] # 편집 용이 
        for i in range(1,len(tokens)):
            try:
                ratings[tokens[2*i-1]] = tokens[2*i] # 음식별 별점 할당. 
                food_list.append(tokens[2*i-1])
            except IndexError: # 빈 값을 입력하려 하는 경우 제외 
                continue
            menus[tokens[0]] = (food_list)
    print("메뉴를 정상적으로 불러왔습니다. ")




def save_file(menus,ratings):
    write_fp = open("./menus.csv","w",encoding = "utf8")

    for category in menus.keys():
        line = [category]
        # 각 category마다 end value를 따로 저장해서 찾아가야하나?? 
        for menu,rating in ratings.items():
            line.append(menu)
            line.append(rating)

        write_line = str(line).replace("'","").replace("[","").replace("]","").replace(" ","")
        write_fp.write(write_line + "\n")

    write_fp.close()
