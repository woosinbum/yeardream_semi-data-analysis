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

#  with webdriver.Chrome(executable_path='/Users/miae/Desktop/yeardream/project/chromedriver') as driver:
driver = webdriver.Chrome(executable_path='/Users/miae/Desktop/yeardream/project/chromedriver')

driver.get("https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do")

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

# 업종별 - 업종개황 -
business_condition_total_list = [] # 전체
business_condition_eat_out_list = [] # 외식
business_condition_wholesale_and_retail_list = [] # 도소매
business_condition_service_list = [] # 서비스

# 업종별 - 가맹본부 변동현황 -
business_headquarters_eat_out_list = [] # 외식
business_headquarters_wholesale_and_retail_list = [] # 도소매
business_headquarters_service_list = [] # 서비스

# 업종별 - 브랜드 변동현황 -
business_brand_eat_out_list = [] # 외식
business_brand_wholesale_and_retail_list = [] # 도소매
business_brand_service_list = [] # 서비스

# 업종별 - 가맹점 변동현황 -
business_affiliate_eat_out_list = [] # 외식
business_affiliate_wholesale_and_retail_list = [] # 도소매
business_affiliate_service_list = [] # 서비스


# 가맹본부별 - 성장성 - 외식 - 
headquarters_growth_eat_out_korean_list = [] # 한식
headquarters_growth_eat_out_bunsik_list = [] # 분식
headquarters_growth_eat_out_chinese_list = [] # 중식
headquarters_growth_eat_out_japanese_list = [] # 일식
headquarters_growth_eat_out_western_list = [] # 서양식
headquarters_growth_eat_out_other_foreign_list = [] # 기타 외국식
headquarters_growth_eat_out_fastfood_list = [] # 패스트푸드
headquarters_growth_eat_out_chicken_list = [] # 치킨
headquarters_growth_eat_out_pizza_list = [] # 피자
headquarters_growth_eat_out_confectionary_and_bakery_list = [] # 제과제빵
headquarters_growth_eat_out_icecream_list = [] # 아이스크림/빙수
headquarters_growth_eat_out_coffee_list = [] # 커피
headquarters_growth_eat_out_drink_list = [] # 음료 (커피 외)
headquarters_growth_eat_out_pub_list = [] # 주점
headquarters_growth_eat_out_other_list = [] # 기타 외식

# 가맹본부별 - 성장성 - 도소매 - 
headquarters_growth_wholesale_and_retail_convenience_list = [] # 편의점
headquarters_growth_wholesale_and_retail_fashion_list = [] # 패션
headquarters_growth_wholesale_and_retail_cosmetics_list = [] # 화장품
headquarters_growth_wholesale_and_retail_agricultural_and_fishery_list = [] # 농수산물
headquarters_growth_wholesale_and_retail_health_food_list = [] # 건강식품
headquarters_growth_wholesale_and_retail_general_retail_store_list = [] # 종합소매점
headquarters_growth_wholesale_and_retail_other_list = [] # 기타 도소매

# 가맹본부별 - 성장성 - 서비스 - 
headquarters_growth_service_subject_education_list = [] # 교과 교육
headquarters_growth_service_foreign_language_education_list = [] # 외국어 교육
headquarters_growth_service_other_education_list = [] # 기타 교육
headquarters_growth_service_infant_excluding_education_list = [] # 유아 관련 (교육 외)
headquarters_growth_service_real_estate_broken_list = [] # 부동산 중개
headquarters_growth_service_lease_list = [] # 임대
headquarters_growth_service_lodgment_list = [] # 숙박
headquarters_growth_service_infant_list = [] # 유아 관련
headquarters_growth_service_sports_list = [] # 스포츠 관련
headquarters_growth_service_beauty_list = [] # 이미용
headquarters_growth_service_car_list = [] # 자동차 관련
headquarters_growth_service_PCroom_list = [] # PC방
headquarters_growth_service_game_list = [] # 오락
headquarters_growth_service_delivery_list = [] # 배달
headquarters_growth_service_glasses_list = [] # 안경
headquarters_growth_service_laundry_list = [] # 세탁
headquarters_growth_service_move_list = [] # 이사
headquarters_growth_service_transit_list = [] # 운송
headquarters_growth_service_pet_list = [] # 반려동물 관련
headquarters_growth_service_pharmacy_list = [] # 약국
headquarters_growth_service_manpower_dispatch_list = [] # 인력 파견
headquarters_growth_service_other_list = [] # 기타 서비스

# 가맹본부별 - 안정성 - 외식 - 
headquarters_stability_eat_out_korean_list = [] # 한식
headquarters_stability_eat_out_bunsik_list = [] # 분식
headquarters_stability_eat_out_chinese_list = [] # 중식
headquarters_stability_eat_out_japanese_list = [] # 일식
headquarters_stability_eat_out_western_list = [] # 서양식
headquarters_stability_eat_out_other_foreign_list = [] # 기타 외국식
headquarters_stability_eat_out_fastfood_list = [] # 패스트푸드
headquarters_stability_eat_out_chicken_list = [] # 치킨
headquarters_stability_eat_out_pizza_list = [] # 피자
headquarters_stability_eat_out_confectionary_and_bakery_list = [] # 제과제빵
headquarters_stability_eat_out_icecream_list = [] # 아이스크림/빙수
headquarters_stability_eat_out_coffee_list = [] # 커피
headquarters_stability_eat_out_drink_list = [] # 음료 (커피 외)
headquarters_stability_eat_out_pub_list = [] # 주점
headquarters_stability_eat_out_other_list = [] # 기타 외식

# 가맹본부별 - 안정성 - 도소매 - 
headquarters_stability_wholesale_and_retail_convenience_list = [] # 편의점
headquarters_stability_wholesale_and_retail_fashion_list = [] # 패션
headquarters_stability_wholesale_and_retail_cosmetics_list = [] # 화장품
headquarters_stability_wholesale_and_retail_agricultural_and_fishery_list = [] # 농수산물
headquarters_stability_wholesale_and_retail_health_food_list = [] # 건강식품
headquarters_stability_wholesale_and_retail_general_retail_store_list = [] # 종합소매점
headquarters_stability_wholesale_and_retail_other_list = [] # 기타 도소매

# 가맹본부별 - 안정성 - 서비스 - 
headquarters_stability_service_subject_education_list = [] # 교과 교육
headquarters_stability_service_foreign_language_education_list = [] # 외국어 교육
headquarters_stability_service_other_education_list = [] # 기타 교육
headquarters_stability_service_infant_excluding_education_list = [] # 유아 관련 (교육 외)
headquarters_stability_service_real_estate_broken_list = [] # 부동산 중개
headquarters_stability_service_lease_list = [] # 임대
headquarters_stability_service_lodgment_list = [] # 숙박
headquarters_stability_service_infant_list = [] # 유아 관련
headquarters_stability_service_sports_list = [] # 스포츠 관련
headquarters_stability_service_beauty_list = [] # 이미용
headquarters_stability_service_car_list = [] # 자동차 관련
headquarters_stability_service_PCroom_list = [] # PC방
headquarters_stability_service_game_list = [] # 오락
headquarters_stability_service_delivery_list = [] # 배달
headquarters_stability_service_glasses_list = [] # 안경
headquarters_stability_service_laundry_list = [] # 세탁
headquarters_stability_service_move_list = [] # 이사
headquarters_stability_service_transit_list = [] # 운송
headquarters_stability_service_pet_list = [] # 반려동물 관련
headquarters_stability_service_pharmacy_list = [] # 약국
headquarters_stability_service_manpower_dispatch_list = [] # 인력 파견
headquarters_stability_service_other_list = [] # 기타 서비스

# 가맹본부별 - 수익성 - 외식 - 
headquarters_profitability_eat_out_korean_list = [] # 한식
headquarters_profitability_eat_out_bunsik_list = [] # 분식
headquarters_profitability_eat_out_chinese_list = [] # 중식
headquarters_profitability_eat_out_japanese_list = [] # 일식
headquarters_profitability_eat_out_western_list = [] # 서양식
headquarters_profitability_eat_out_other_foreign_list = [] # 기타 외국식
headquarters_profitability_eat_out_fastfood_list = [] # 패스트푸드
headquarters_profitability_eat_out_chicken_list = [] # 치킨
headquarters_profitability_eat_out_pizza_list = [] # 피자
headquarters_profitability_eat_out_confectionary_and_bakery_list = [] # 제과제빵
headquarters_profitability_eat_out_icecream_list = [] # 아이스크림/빙수
headquarters_profitability_eat_out_coffee_list = [] # 커피
headquarters_profitability_eat_out_drink_list = [] # 음료 (커피 외)
headquarters_profitability_eat_out_pub_list = [] # 주점
headquarters_profitability_eat_out_other_list = [] # 기타 외식

# 가맹본부별 - 수익성 - 도소매 - 
headquarters_profitability_wholesale_and_retail_convenience_list = [] # 편의점
headquarters_profitability_wholesale_and_retail_fashion_list = [] # 패션
headquarters_profitability_wholesale_and_retail_cosmetics_list = [] # 화장품
headquarters_profitability_wholesale_and_retail_agricultural_and_fishery_list = [] # 농수산물
headquarters_profitability_wholesale_and_retail_health_food_list = [] # 건강식품
headquarters_profitability_wholesale_and_retail_general_retail_store_list = [] # 종합소매점
headquarters_profitability_wholesale_and_retail_other_list = [] # 기타 도소매

# 가맹본부별 - 수익성 - 서비스 - 
headquarters_profitability_service_subject_education_list = [] # 교과 교육
headquarters_profitability_service_foreign_language_education_list = [] # 외국어 교육
headquarters_profitability_service_other_education_list = [] # 기타 교육
headquarters_profitability_service_infant_excluding_education_list = [] # 유아 관련 (교육 외)
headquarters_profitability_service_real_estate_broken_list = [] # 부동산 중개
headquarters_profitability_service_lease_list = [] # 임대
headquarters_profitability_service_lodgment_list = [] # 숙박
headquarters_profitability_service_infant_list = [] # 유아 관련
headquarters_profitability_service_sports_list = [] # 스포츠 관련
headquarters_profitability_service_beauty_list = [] # 이미용
headquarters_profitability_service_car_list = [] # 자동차 관련
headquarters_profitability_service_PCroom_list = [] # PC방
headquarters_profitability_service_game_list = [] # 오락
headquarters_profitability_service_delivery_list = [] # 배달
headquarters_profitability_service_glasses_list = [] # 안경
headquarters_profitability_service_laundry_list = [] # 세탁
headquarters_profitability_service_move_list = [] # 이사
headquarters_profitability_service_transit_list = [] # 운송
headquarters_profitability_service_pet_list = [] # 반려동물 관련
headquarters_profitability_service_pharmacy_list = [] # 약국
headquarters_profitability_service_manpower_dispatch_list = [] # 인력 파견
headquarters_profitability_service_other_list = [] # 기타 서비스


# 브랜드별 - 브랜드 개요 - 외식 - 
brand_outline_eat_out_korean_list = [] # 한식
brand_outline_eat_out_bunsik_list = [] # 분식
brand_outline_eat_out_chinese_list = [] # 중식
brand_outline_eat_out_japanese_list = [] # 일식
brand_outline_eat_out_western_list = [] # 서양식
brand_outline_eat_out_other_foreign_list = [] # 기타 외국식
brand_outline_eat_out_fastfood_list = [] # 패스트푸드
brand_outline_eat_out_chicken_list = [] # 치킨
brand_outline_eat_out_pizza_list = [] # 피자
brand_outline_eat_out_confectionary_and_bakery_list = [] # 제과제빵
brand_outline_eat_out_icecream_list = [] # 아이스크림/빙수
brand_outline_eat_out_coffee_list = [] # 커피
brand_outline_eat_out_drink_list = [] # 음료 (커피 외)
brand_outline_eat_out_pub_list = [] # 주점
brand_outline_eat_out_other_list = [] # 기타 외식

# 브랜드별 - 브랜드 개요 - 도소매 - 
brand_outline_wholesale_and_retail_convenience_list = [] # 편의점
brand_outline_wholesale_and_retail_fashion_list = [] # 패션
brand_outline_wholesale_and_retail_cosmetics_list = [] # 화장품
brand_outline_wholesale_and_retail_agricultural_and_fishery_list = [] # 농수산물
brand_outline_wholesale_and_retail_health_food_list = [] # 건강식품
brand_outline_wholesale_and_retail_general_retail_store_list = [] # 종합소매점
brand_outline_wholesale_and_retail_other_list = [] # 기타 도소매

# 브랜드별 - 브랜드 개요 - 서비스 - 
brand_outline_service_subject_education_list = [] # 교과 교육
brand_outline_service_foreign_language_education_list = [] # 외국어 교육
brand_outline_service_other_education_list = [] # 기타 교육
brand_outline_service_infant_excluding_education_list = [] # 유아 관련 (교육 외)
brand_outline_service_real_estate_broken_list = [] # 부동산 중개
brand_outline_service_lease_list = [] # 임대
brand_outline_service_lodgment_list = [] # 숙박
brand_outline_service_infant_list = [] # 유아 관련
brand_outline_service_sports_list = [] # 스포츠 관련
brand_outline_service_beauty_list = [] # 이미용
brand_outline_service_car_list = [] # 자동차 관련
brand_outline_service_PCroom_list = [] # PC방
brand_outline_service_game_list = [] # 오락
brand_outline_service_delivery_list = [] # 배달
brand_outline_service_glasses_list = [] # 안경
brand_outline_service_laundry_list = [] # 세탁
brand_outline_service_move_list = [] # 이사
brand_outline_service_transit_list = [] # 운송
brand_outline_service_pet_list = [] # 반려동물 관련
brand_outline_service_pharmacy_list = [] # 약국
brand_outline_service_manpower_dispatch_list = [] # 인력 파견
brand_outline_service_other_list = [] # 기타 서비스

# 브랜드별 - 가맹점 현황 정보 - 외식 -
brand_affiliate_condition_eat_out_korean_list = [] # 한식
brand_affiliate_condition_eat_out_bunsik_list = [] # 분식
brand_affiliate_condition_eat_out_chinese_list = [] # 중식
brand_affiliate_condition_eat_out_japanese_list = [] # 일식
brand_affiliate_condition_eat_out_western_list = [] # 서양식
brand_affiliate_condition_eat_out_other_foreign_list = [] # 기타 외국식
brand_affiliate_condition_eat_out_fastfood_list = [] # 패스트푸드
brand_affiliate_condition_eat_out_chicken_list = [] # 치킨
brand_affiliate_condition_eat_out_pizza_list = [] # 피자
brand_affiliate_condition_eat_out_confectionary_and_bakery_list = [] # 제과제빵
brand_affiliate_condition_eat_out_icecream_list = [] # 아이스크림/빙수
brand_affiliate_condition_eat_out_coffee_list = [] # 커피
brand_affiliate_condition_eat_out_drink_list = [] # 음료 (커피 외)
brand_affiliate_condition_eat_out_pub_list = [] # 주점
brand_affiliate_condition_eat_out_other_list = [] # 기타 외식

# 브랜드별 - 가맹점 현황 정보 - 도소매 - 
brand_affiliate_condition_wholesale_and_retail_convenience_list = [] # 편의점
brand_affiliate_condition_wholesale_and_retail_fashion_list = [] # 패션
brand_affiliate_condition_wholesale_and_retail_cosmetics_list = [] # 화장품
brand_affiliate_condition_wholesale_and_retail_agricultural_and_fishery_list = [] # 농수산물
brand_affiliate_condition_wholesale_and_retail_health_food_list = [] # 건강식품
brand_affiliate_condition_wholesale_and_retail_general_retail_store_list = [] # 종합소매점
brand_affiliate_condition_wholesale_and_retail_other_list = [] # 기타 도소매

# 브랜드별 - 가맹점 현황 정보 - 서비스 - 
brand_affiliate_condition_service_subject_education_list = [] # 교과 교육
brand_affiliate_condition_service_foreign_language_education_list = [] # 외국어 교육
brand_affiliate_condition_service_other_education_list = [] # 기타 교육
brand_affiliate_condition_service_infant_excluding_education_list = [] # 유아 관련 (교육 외)
brand_affiliate_condition_service_real_estate_broken_list = [] # 부동산 중개
brand_affiliate_condition_service_lease_list = [] # 임대
brand_affiliate_condition_service_lodgment_list = [] # 숙박
brand_affiliate_condition_service_infant_list = [] # 유아 관련
brand_affiliate_condition_service_sports_list = [] # 스포츠 관련
brand_affiliate_condition_service_beauty_list = [] # 이미용
brand_affiliate_condition_service_car_list = [] # 자동차 관련
brand_affiliate_condition_service_PCroom_list = [] # PC방
brand_affiliate_condition_service_game_list = [] # 오락
brand_affiliate_condition_service_delivery_list = [] # 배달
brand_affiliate_condition_service_glasses_list = [] # 안경
brand_affiliate_condition_service_laundry_list = [] # 세탁
brand_affiliate_condition_service_move_list = [] # 이사
brand_affiliate_condition_service_transit_list = [] # 운송
brand_affiliate_condition_service_pet_list = [] # 반려동물 관련
brand_affiliate_condition_service_pharmacy_list = [] # 약국
brand_affiliate_condition_service_manpower_dispatch_list = [] # 인력 파견
brand_affiliate_condition_service_other_list = [] # 기타 서비스

# 브랜드별 - 가맹점 창업 비용 - 외식 -
brand_affiliate_start_up_cost_eat_out_korean_list = [] # 한식
brand_affiliate_start_up_cost_eat_out_bunsik_list = [] # 분식
brand_affiliate_start_up_cost_eat_out_chinese_list = [] # 중식
brand_affiliate_start_up_cost_eat_out_japanese_list = [] # 일식
brand_affiliate_start_up_cost_eat_out_western_list = [] # 서양식
brand_affiliate_start_up_cost_eat_out_other_foreign_list = [] # 기타 외국식
brand_affiliate_start_up_cost_eat_out_fastfood_list = [] # 패스트푸드
brand_affiliate_start_up_cost_eat_out_chicken_list = [] # 치킨
brand_affiliate_start_up_cost_eat_out_pizza_list = [] # 피자
brand_affiliate_start_up_cost_eat_out_confectionary_and_bakery_list = [] # 제과제빵
brand_affiliate_start_up_cost_eat_out_icecream_list = [] # 아이스크림/빙수
brand_affiliate_start_up_cost_eat_out_coffee_list = [] # 커피
brand_affiliate_start_up_cost_eat_out_drink_list = [] # 음료 (커피 외)
brand_affiliate_start_up_cost_eat_out_pub_list = [] # 주점
brand_affiliate_start_up_cost_eat_out_other_list = [] # 기타 외식

# 브랜드별 - 가맹점 창업 비용 - 도소매 - 
brand_affiliate_start_up_cost_wholesale_and_retail_convenience_list = [] # 편의점
brand_affiliate_start_up_cost_wholesale_and_retail_fashion_list = [] # 패션
brand_affiliate_start_up_cost_wholesale_and_retail_cosmetics_list = [] # 화장품
brand_affiliate_start_up_cost_wholesale_and_retail_agricultural_and_fishery_list = [] # 농수산물
brand_affiliate_start_up_cost_wholesale_and_retail_health_food_list = [] # 건강식품
brand_affiliate_start_up_cost_wholesale_and_retail_general_retail_store_list = [] # 종합소매점
brand_affiliate_start_up_cost_wholesale_and_retail_other_list = [] # 기타 도소매

# 브랜드별 - 가맹점 창업 비용 - 서비스 - 
brand_affiliate_start_up_cost_service_subject_education_list = [] # 교과 교육
brand_affiliate_start_up_cost_service_foreign_language_education_list = [] # 외국어 교육
brand_affiliate_start_up_cost_service_other_education_list = [] # 기타 교육
brand_affiliate_start_up_cost_service_infant_excluding_education_list = [] # 유아 관련 (교육 외)
brand_affiliate_start_up_cost_service_real_estate_broken_list = [] # 부동산 중개
brand_affiliate_start_up_cost_service_lease_list = [] # 임대
brand_affiliate_start_up_cost_service_lodgment_list = [] # 숙박
brand_affiliate_start_up_cost_service_infant_list = [] # 유아 관련
brand_affiliate_start_up_cost_service_sports_list = [] # 스포츠 관련
brand_affiliate_start_up_cost_service_beauty_list = [] # 이미용
brand_affiliate_start_up_cost_service_car_list = [] # 자동차 관련
brand_affiliate_start_up_cost_service_PCroom_list = [] # PC방
brand_affiliate_start_up_cost_service_game_list = [] # 오락
brand_affiliate_start_up_cost_service_delivery_list = [] # 배달
brand_affiliate_start_up_cost_service_glasses_list = [] # 안경
brand_affiliate_start_up_cost_service_laundry_list = [] # 세탁
brand_affiliate_start_up_cost_service_move_list = [] # 이사
brand_affiliate_start_up_cost_service_transit_list = [] # 운송
brand_affiliate_start_up_cost_service_pet_list = [] # 반려동물 관련
brand_affiliate_start_up_cost_service_pharmacy_list = [] # 약국
brand_affiliate_start_up_cost_service_manpower_dispatch_list = [] # 인력 파견
brand_affiliate_start_up_cost_service_other_list = [] # 기타 서비스


search_condition = Select(driver.find_element_by_id('searchCondition'))
search_condition_sub = Select(driver.find_element_by_id('selListType'))
sel_upjong = Select(driver.find_element_by_id('selUpjong'))
sel_upjong_sub = Select(driver.find_element_by_id('selIndus'))

search_btn = driver.find_element_by_xpath('//*[@id="frm"]/div[4]/input[2]')

# for search_condition_value in search_condition_values:
#     search_condition.select_by_value(search_condition_value)

#     if search_condition_value == '1': # 업종별
#         for type_of_business_value in type_of_business_values:
#             search_condition_sub.select_by_value(type_of_business_value)

#             if type_of_business_value == 'listHq01': # 업종개황
#                 for upjong_value in upjong_values:
#                     if upjong_value == '21': # 외식
#                         # 업종, 가맹본부수, 브랜드수, 가맹점수, 직영점수
#                         table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')

#                         for tr in table:
#                             business_condition_eat_out_dic = {
#                                 '업종': tr[0].text,

#                             }




search_condition.select_by_value('1')
search_condition_sub.select_by_value('listIndus01')
# sel_upjong.select_by_value('21')
# driver.implicitly_wait(1) # 암시적 대기
# sel_upjong_sub.select_by_value('G1')
search_btn.click()
driver.implicitly_wait(1) # 암시적 대기

table = driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody')
tr = table.find_elements_by_tag_name('tr')

for td in tr:
    td = td.text.split(' ')

    business_condition_total_list.append({
        '업종': td[0],
        '가맹본부수': td[1],
        '브랜드수': td[2],
        '가맹점수': td[3],
        '직영점수': td[4]
    })

print(business_condition_total_list)

driver.close()
