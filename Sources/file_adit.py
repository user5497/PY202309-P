import pandas as pd

menus = {'한식':[{'불고기': ['0','d'], '오징어 두루치기': ['0','d'], '닭볶음': ['0','d'], '쌈밥': ['0','d'], '비빔밥': ['0','d'], '생선구이': ['0','d'], '낚지볶음': ['0','d'], '게장': ['0','d'], '떡갈비': ['0','d']}], 
           '찌개':[{'김치찌개': ['0','d'], '순두부찌개': ['0','d'], '된장찌개': ['0','d'], '부대찌개': '0', '동 태찌개': ['0','d'], '청국장': ['0','d'], '갈비탕': ['0','d'], '추어탕': ['0','d'], '삼계탕': ['0','d']}],
           '중식':[{'짜장면': ['0','d'], '짬뽕': ['0','d'], '볶음밥': ['0','d'], '탕수육': ['0','d'], '마파두부': ['0','d'], '양장피': ['0','d'], '깐풍기': ['0','d'], '유린기': ['0','d'], '고추잡채': ['0','d']}],
           '양식':[{'토마토 스파게티': ['0','d'], ' 봉골레': ['0','d'], '크림파스타': ['0','d'], '피자': ['0','d'], '함박스테이크': ['0','d'], '리조또': ['0','d'], '스테이크': ['0','d'], '햄버거': ['0','d'], '시저 샐러드': ['0','d']}],
           '일식':[{'초밥': ['0','d'], '라멘': '0', '낫또': ['0','d'], '오니기리': ['0','d'], '덮밥': ['0','d'], '우동': ['0','d'], '메밀소바': ['0','d'], '돈카츠': ['0','d']}],
           '간편식':[{'편의점도시락': ['0','d'], '샌드위치': ['0','d'], '토스트': ['0','d'], '샐러드': ['0','d'], '김밥': ['0','d'], '떡볶이': ['0','d'], '핫도그': ['0','d'], '밥버거': ['0','d'], '시리얼': ['0','d']}],
           '기타':[{'쌀국수': ['0','d'], '팟타이': ['0','d'], '카레': ['0','d'], '찜닭': ['0','d'], '수제비': ['0','d'], '칼국 수': ['0','d'], '아구찜': ['0','d'], '닭갈비': ['0','d'], '월남쌈': ['0','d']}]}


# 여기가 메인일 때만 실행하기. 
# 세부 내용 수정하기 
data = []

for category, menu_infos in menus.items():
    print("menu_infos",menu_infos)
    for menu_name,menu_info in menu_infos[0].items():
        print("menu_info",menu_info)
        print("menu_name",menu_name)
        row = {"Category": category, "Menu": menu_name,
              "ratings":menu_info[0], "Memo":menu_info[1]}
        data.append(row)

df = pd.DataFrame(data)

print(data)