# 기존 mongodb collection을 이용해 상권_코드, 상권_코드_명만 새 collection 생성
from pymongo import MongoClient

client = MongoClient("mongodb+srv://user1:uZGuuMyRngM3izgG@cluster0.cu0c3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("elice")
col = db.get_collection("commercial_area")

col1 = db.get_collection('sales_rate_gender')

commercial_area_codes = col1.distinct("상권_코드")
commercial_area_names = col1.distinct("상권_코드_명")

commercial_areas = []

for i in range(len(commercial_area_codes)):
    commercial_areas.append({
        "상권_코드": commercial_area_codes[i],
        "상권_코드_명": commercial_area_names[i]
    })

# 데이터 삽입
col.insert_many(commercial_areas)

# 데이터 잘 들어갔는지 확인
for commercial_area in col.find():
    print(commercial_area)
