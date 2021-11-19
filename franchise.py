# 업종별: type_of_business
    ## 업종개황: condition
    ## 가맹본부 변동현황: headquarters
    ## 브랜드 변동현황: brand_
    ## 가맹점 변동현황: affiliate

# 가맹본부별: headquarters
    ## 성장성: growth
    ## 안정성: stability
    ## 수익성: profitability

# 브랜드별: brand
    ## 브랜드 개요: outline
    ## 가맹점 현황 정보: affiliate_condition
    ## 가맹점 창업 비용: affiliate_start_up_cost

# 업종
    ## 외식: eat_out
        ### 한식: korean
        ### 분식: bunsik
        ### 중식: chinese
        ### 일식: japanese
        ### 서양식: western
        ### 기타 외국식: other_foreign
        ### 패스트푸드: fastfood
        ### 치킨: chicken
        ### 피자: pizza
        ### 제과제빵: confectionery_and_bakery
        ### 아이스크림/빙수: icecream
        ### 커피: coffee
        ### 음료(커피 외): drink
        ### 주점: pub
        ### 기타 외식: other

    ## 도소매: wholesale_and_retail
        ### 편의점: convenience
        ### 의류/패션: fashion
        ### 화장품: cosmetics
        ### 농수산물: agricultural_and_fishery
        ### 건강식품: health_food
        ### 종합소매점: general_retail_store
        ### 기타도소매: other_wholesale_and_retail

    ## 서비스: service
        ### 교과 교육: subject_education
        ### 외국어 교육: foreign_language_education
        ### 기타 교육: other_education
        ### 유아 관련 (교육 외) + 유아 관련: infant
        ### 부동산 중개: real_estate_broken
        ### 임대: lease
        ### 숙박: lodgment
        ### 스포츠 관련: sports
        ### 이미용: beauty
        ### 자동차: car
        ### PC방: PCroom
        ### 오락: game
        ### 배달: delivery
        ### 안경: glasses
        ### 세탁: laundry
        ### 이사: move
        ### 운송: transit
        ### 반려동물 관련: pet
        ### 약국: pharmacy
        ### 인력 파견: manpower_dispatch
        ### 기타 서비스: other_service

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# from pymongo import MongoClient

# connection = client = MongoClient("mongodb+srv://user1:uZGuuMyRngM3izgG@cluster0.cu0c3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = connection.get_database('elice')
# col = db.get_collection('franchise')

# def set_business_condition(driver):
#     table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')
#     tr = table.find_elements_by_tag_name('tr')
#     tmp = []

#     for td in tr:
#         td = td.text.split(' ')
        
#         tmp.append({
#             "업종": td[0],
#             "가맹본부수": td[1],
#             "브랜드수": td[2],
#             "가맹점수": td[3],
#             "직영점수": td[4]
#         })
    
#     print(tmp)
    
#     return tmp


with webdriver.Chrome(executable_path='/Users/miae/Desktop/yeardream/project/chromedriver') as driver:
# driver = webdriver.Chrome(executable_path='/Users/miae/Desktop/yeardream/project/chromedriver')

    driver.get("https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do")

    business_condition_total_list = []
    business_condition_eat_out_list = []
    business_condition_wholesale_and_retail_list = []
    business_condition_service_list = []

    search_condition_values = ['1', '2', '3'] # 업종별, 가맹본부별, 브랜드별
    # search_condition_sub_values
    type_of_business_values = ['listIndus01', 'listIndus02', 'listIndus03', 'listIndus04'] # 업종별 하위 분류
    headquarters_values = ['listHq01', 'listHq02', 'listHq03'] # 가맹본부별 하위 분류
    brand_values = ['listBrand01', 'listBrand02', 'listBrand03'] # 브랜드별 하위 분류

    upjong_values = ['21', '22', '23'] # 외식, 도소매, 서비스
    # upjong_sub_values
    eat_out_values = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1'] # 외식 - 중분류
    wholesale_and_retail_values = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2'] # 도소매 - 중분류
    service_values = ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'O ', 'H3', 'I3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3', 'P3', 'Q3', 'R3', 'S3', 'T3', 'U3'] # 서비스 - 중분류

    search_condition = Select(driver.find_element_by_xpath('//*[@id="searchCondition"]'))
    search_condition_sub = Select(driver.find_element_by_xpath('//*[@id="selListType"]'))
    sel_upjong = Select(driver.find_element_by_xpath('//*[@id="selUpjong"]'))
    sel_upjong_sub = Select(driver.find_element_by_xpath('//*[@id="selIndus"]'))

    search_btn = driver.find_element_by_xpath('//*[@id="frm"]/div[4]/input[2]')

    search_condition.select_by_value(search_condition_values[0])
    driver.implicitly_wait(1)
    search_condition_sub.select_by_value(type_of_business_values[0])

    sel_upjong.select_by_value('21')
    driver.implicitly_wait(1)
    search_btn.click()

    table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')
    tr = table.find_elements_by_tag_name('tr')

    for td in tr:
        td = td.text.split(' ')
        
        business_condition_eat_out_list.append({
            "업종": td[0],
            "가맹본부수": td[1],
            "브랜드수": td[2],
            "가맹점수": td[3],
            "직영점수": td[4]
        })

    sel_upjong.select_by_value('22').click()
    driver.implicitly_wait(1)
    search_btn.click()

    table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')
    tr = table.find_elements_by_tag_name('tr')

    for td in tr:
        td = td.text.split(' ')
        
        business_condition_wholesale_and_retail_list.append({
            "업종": td[0],
            "가맹본부수": td[1],
            "브랜드수": td[2],
            "가맹점수": td[3],
            "직영점수": td[4]
        })
    
    print(business_condition_eat_out_list)
    print(business_condition_wholesale_and_retail_list)

    # search_condition.select_by_value('1')
    # search_condition_sub.select_by_value('listIndus01')
    # sel_upjong.select_by_value('21')
    # driver.implicitly_wait(1) # 암시적 대기
    # sel_upjong_sub.select_by_value('G1')
    # search_btn.click()
    # driver.implicitly_wait(1) # 암시적 대기

    # for search_condition_value in search_condition_values:
    #     search_condition.select_by_value(search_condition_value)
    #     driver.implicitly_wait(1) # 암시적 대기

    #     if search_condition_value == '1': # 업종별
    #         for type_of_business_value in type_of_business_values:
    #             search_condition_sub.select_by_value(type_of_business_value)

    #             if type_of_business_value == 'listIndus01': # 업종개황
                    # search_btn.click()
                    # business_condition_total_list = set_business_condition(driver) # 전체

                    # table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')
                    # tr = table.find_elements_by_tag_name('tr')

                    # for td in tr:
                    #     td = td.text.split(' ')
                        
                    #     business_condition_total_list.append({
                    #         "업종": td[0],
                    #         "가맹본부수": td[1],
                    #         "브랜드수": td[2],
                    #         "가맹점수": td[3],
                    #         "직영점수": td[4]
                    #     })

                    # business_condition_eat_out_list = set_business_condition(driver)

                    # for upjong_value in upjong_values: # 업종별
                    #     sel_upjong.select_by_value(upjong_value)
                    #     search_btn.click()

                    #     driver.implicitly_wait(10)

                    #     table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')
                    #     tr = table.find_elements_by_tag_name('tr')

                    #     # if upjong_value == '21':
                    #     for td in tr:
                    #         td = td.text.split(' ')
                            
                    #         business_condition_eat_out_list.append({
                    #             "업종": td[0],
                    #             "가맹본부수": td[1],
                    #             "브랜드수": td[2],
                    #             "가맹점수": td[3],
                    #             "직영점수": td[4]
                    #         })
                        # elif upjong_value == '22':
                        #     for td in tr:
                        #         td = td.text.split(' ')
                                
                        #         business_condition_wholesale_and_retail_list.append({
                        #             "업종": td[0],
                        #             "가맹본부수": td[1],
                        #             "브랜드수": td[2],
                        #             "가맹점수": td[3],
                        #             "직영점수": td[4]
                        #         })
                        # else:
                        #     business_condition_service_list = tmp


    # print(business_condition_total_list)
    # print(business_condition_eat_out_list)
    # print(business_condition_wholesale_and_retail_list)
    # print(business_condition_service_list)


# search_condition.select_by_value('1')
# search_condition_sub.select_by_value('listIndus01')
# sel_upjong.select_by_value('21')
# driver.implicitly_wait(1) # 암시적 대기
# sel_upjong_sub.select_by_value('G1')
# search_btn.click()
# driver.implicitly_wait(1) # 암시적 대기

# 형식
# {
#     "type_of_business": {
#         "condition": [{
#             "total": total, 
#             "eat_out": [

#             ], "wholesale_and_retail": [

#             ], "service": [
                
#             ]
#         }], "business_condition": [{
            
#         }]
#     }
# }
