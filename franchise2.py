from selenium import webdriver
from selenium.webdriver.support.ui import Select

from pymongo import MongoClient

connection = MongoClient("mongodb+srv://user1:uZGuuMyRngM3izgG@cluster0.cu0c3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = connection.get_database("elice")
col = db.get_collection("franchise2")

search_condition_values = ["2", "3"]  # 업종별, 가맹본부별, 브랜드별
# search_condition_sub_values
# type_of_business_values = ["listIndus01", "listIndus02", "listIndus03", "listIndus04"]  # 업종별 하위 분류
# headquarters_values = ["listHq01", "listHq02", "listHq03"]  # 가맹본부별 하위 분류
# brand_values = ["listBrand01", "listBrand02", "listBrand03"]  # 브랜드별 하위 분류
type_of_business_values = ["listIndus04"]  # 업종별 하위 분류
headquarters_values = ["listHq02", "listHq03"]  # 가맹본부별 하위 분류
brand_values = ["listBrand02", "listBrand03"]  # 브랜드별 하위 분류

upjong_values = ["21", "22", "23"]  # 전체, 외식, 도소매, 서비스
# upjong_sub_values
eat_out_values = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1"]  # 외식 - 중분류
wholesale_and_retail_values = ["A2", "B2", "C2", "D2", "E2", "F2", "G2"]  # 도소매 - 중분류
service_values = ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "O ", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3"]  # 서비스 - 중분류

# type_of_business
# condition_menu = ["업종", "가맹본부수", "브랜드수", "가맹점수", "직영점수"]
# headquarters_menu = ["업종", "가맹본부 증가수(증가율)", "신규등록 가맹본부수(신규등록률)", "등록취소 가맹본부수(등록취소율)", "가맹본부 평균 영업기간"]
# brand_menu = ["브랜드 증가수(증가율)", "브랜드 신규등록수(신규등록률)", "브랜드 소멸수(소멸률)", "브랜드 평균 영업기간"]
affiliate_menu = ["업종", "가맹점 증가수(증가율)", "가맹점 신규개점수(개점률)", "가맹점 폐점수(폐점률)"]
# headquarters
# growth_menu = ["상호", "자산", "매출액", "영업이익", "총자산증가율", "매출액증가율", "영업이익증가율"]
stability_menu = ["상호", "자산", "자본", "부채", "부채비율(부채/자본)", "자기자본비율(자본/자산)", "법위반횟수(최근 3년)"]
profitability_menu = ["상호", "자본", "매출액", "영업이익", "당기순이익", "영업이익률(영업이익/매출액)", "매출액 순이익률(당기순이익/매출액)", "자기자본 순이익률(당기순이익/자본)"]
# brand
# outline_menu = ["브랜드", "상호", "가맹사업 개시일", "가맹사업 년수", "가맹점수", "가맹본부 임직원수"]
affiliate_condition_menu = ["브랜드", "상호", "가맹점수", "신규개점", "계약종료", "계약해지", "명의변경", "가맹점 평균매출액", "가맹점 면적(3.3㎡)당 평균 매출액"]
affiliate_start_up_cost_menu = ["브랜드", "상호", "가입비(가맹비)", "교육비", "보증금", "기타비용(인테리어 비용포함)", "합계(창업비용지수)", "면적당(3.3㎡) 비용", "기준면적(㎡)", "총 비용"]

search_condition_dic = {
    "1": "업종별",
    "2": "가맹본부별",
    "3": "브랜드별"
}

search_condition_sub_dic = {
    # "listIndus01": "업종개황",
    # "listIndus02": "가맹본부 변동현황",
    # "listIndus03": "브랜드 변동현황",
    "listIndus04": "가맹점 변동현황",
    # "listHq01": "성장성",
    "listHq02": "안정성",
    "listHq03": "수익성",
    # "listBrand01": "브랜드 개요",
    "listBrand02": "가맹점 현황 정보",
    "listBrand03": "가맹점 창업비용"
}

upjong_dic = {
    "21": "외식",
    "22": "도소매",
    "23": "서비스"
}

upjong_sub_dic = {
    "0": "전체",
    "A1": "한식",
    "B1": "분식",
    "C1": "중식",
    "D1": "일식",
    "E1": "서양식",
    "F1": "기타 외국식",
    "G1": "패스트푸드",
    "H1": "치킨",
    "I1": "피자",
    "J1": "제과제빵",
    "K1": "아이스크림/빙수",
    "L1": "커피",
    "M1": "음료(커피 외)",
    "N1": "주점",
    "O1": "기타 외식",
    "A2": "편의점",
    "B2": "패션",
    "C2": "화장품",
    "D2": "농수산물",
    "E2": "건강식품",
    "F2": "종합소매점",
    "G2": "기타도소매",
    "A3": "교과 교육",
    "B3": "외국어 교육",
    "C3": "기타 교육",
    "D3": "유아 관련(교육 외)",
    "E3": "부동산 중개",
    "F3": "임대",
    "G3": "숙박",
    "O ": "유아 관련",
    "H3": "스포츠 관련",
    "I3": "이미용",
    "J3": "자동차 관련",
    "K3": "PC방",
    "L3": "오락",
    "M3": "배달",
    "N3": "안경",
    "O3": "세탁",
    "P3": "이사",
    "Q3": "운송",
    "R3": "반려동물 관련",
    "S3": "약국",
    "T3": "인력 파견",
    "U3": "기타 서비스"
}

def page_crawling(search_condition_value, search_condition_sub_value, upjong_value, upjong_sub_value):
    search_condition_text = search_condition_dic[search_condition_value]
    search_condition_sub_text = search_condition_sub_dic[search_condition_sub_value]
    upjong_text = upjong_dic[upjong_value]
    upjong_sub_text = upjong_sub_dic[upjong_sub_value]

    with webdriver.Chrome(executable_path="/Users/miae/Desktop/yeardream/project/chromedriver") as driver:
        driver.get("https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do")

        # 연결 비공개 에러 
        # btn1 = driver.find_element_by_xpath("//*[@id="details-button"]").click()
        # driver.implicitly_wait(1)
        # a_link = driver.find_element_by_xpath("//*[@id="proceed-link"]").click()
        # driver.implicitly_wait(10)

        search_condition = Select(driver.find_element_by_xpath("//*[@id='searchCondition']"))
        search_condition_sub = Select(driver.find_element_by_xpath("//*[@id='selListType']"))
        upjong = Select(driver.find_element_by_xpath("//*[@id='selUpjong']"))
        upjong_sub = Select(driver.find_element_by_xpath("//*[@id='selIndus']"))

        search_btn = driver.find_element_by_xpath("//*[@id='frm']/div[4]/input[2]")

        search_condition.select_by_value(search_condition_value)
        driver.implicitly_wait(1)  # 암시적 대기
        search_condition_sub.select_by_value(search_condition_sub_value)

        if upjong_value != "0":  # 업종 대분류: 외식, 도소매, 서비스
            upjong.select_by_value(upjong_value)

            if upjong_sub_value != "0":  # 업종 소분류: 전체 X
                driver.implicitly_wait(1)
                upjong_sub.select_by_value(upjong_sub_value)
        
        search_btn.click()
    
        table = driver.find_element_by_xpath("//*[@id='content']/div[4]/table/tbody")
        
        for tr in table.find_elements_by_tag_name("tr"):
            td = tr.find_elements_by_tag_name("td")

            # search_condition_value == "1"
            if search_condition_sub_value == "listIndus04":
                arr = affiliate_menu
            # search_condition_value == "2"
            elif search_condition_sub_value == "listHq02":
                arr = stability_menu
            elif search_condition_sub_value == "listHq03":
                arr = profitability_menu
            # search_condition_value == "3"
            elif search_condition_sub_value == "listBrand02":
                arr = affiliate_condition_menu
            elif search_condition_sub_value == "listBrand03":
                arr = affiliate_start_up_cost_menu
            
            tmp_dic = {
                "비교 항목": search_condition_text,
                "세부 비교 항목": search_condition_sub_text,
                "업종 대분류": upjong_text,
                "업종 소분류": upjong_sub_text
            }

            for i in range(len(arr)):
                # 마지막 컬럼 값이 없으면 td[i]가 아예 존재하지 않음
                if len(td) == i: 
                    break
                    
                td[i] = td[i].text
                
                if search_condition_value == "1":
                    tmp_dic[arr[i]] = td[i].replace("\n", " ")
                # else:
                #     if search_condition_value == "3" and search_condition_sub_value == "listBrand03" and upjong_value == "23" and upjong_sub_value == "Q3":
                #         if i >= 7:
                #             tmp_dic[arr[i]] = 0

                #             continue

                    if ((search_condition_value == "2" and i >= 1) or (search_condition_value == "3" and i >= 2)):
                        if i == 6:
                            td[i] = td[i].replace("\n", " ")
                            td[i] = td[i].split(" ")[0]
                        
                        if "," in td[i]:
                            td[i] = td[i].replace(",", "")

                        if "%" in td[i]:
                            td[i] = td[i].replace("%", "")
                        
                        if "." in td[i]:
                            tmp_dic[arr[i]] = float(td[i])
                        elif td[i] == "":
                            tmp_dic[arr[i]] = 0
                        else:
                            tmp_dic[arr[i]] = int(td[i])
                    else:
                        tmp_dic[arr[i]] = td[i]
                    
            try:
                col.insert_one(tmp_dic)
            except Exception as e:
                print(e)


for search_condition_value in search_condition_values:  # 비교 항목
    if search_condition_value == "1":
        search_condition_sub_arr = type_of_business_values
    elif search_condition_value == "2":
        search_condition_sub_arr = headquarters_values
    elif search_condition_value == "3":
        search_condition_sub_arr = brand_values

    for search_condition_sub_value in search_condition_sub_arr:  # 비교 세부 항목
        for upjong_value in upjong_values:  # 업종 대분류
            if upjong_value == "21":
                upjong_sub_arr = eat_out_values
            elif upjong_value == "22":
                upjong_sub_arr = wholesale_and_retail_values
            elif upjong_value == "23":
                upjong_sub_arr = service_values

            # 비교 항목이 업종별일 때
            # 업종 대분류: 전체(0)/외식/도소매/서비스 -> 업종 소분류: 전체
            if search_condition_value == "1":
                upjong_sub_value = "0"
                page_crawling(search_condition_value, search_condition_sub_value, upjong_value, upjong_sub_value)
            else:
                for upjong_sub_value in upjong_sub_arr:
                    page_crawling(search_condition_value, search_condition_sub_value, upjong_value, upjong_sub_value)
