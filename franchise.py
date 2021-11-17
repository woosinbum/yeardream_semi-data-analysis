# 업종별: type_of_business
    ## 업종개황: condition
    ## 가맹본부 변동현황: franchise_headquarters_condition
    ## 브랜드 변동현황: brand_condition
    ## 가맹점 변동현황: affiliate_condition

# 가맹본부별: headquarters
    ## 성장성: growth
    ## 안정성: stability
    ## 수익성: profitability

# 브랜드별: brand
    ## 브랜드 개요: outline
    ## 가맹점 현황 정보: affiliate_condition_information
    ## 가맹점 창업 비용: affiliate_start_up_cost

# 업종
    ## 외식: eat_out
        ### 한식: korean_food
        ### 분식: bunsik
        ### 중식: chinese_food
        ### 일식: japanese_food
        ### 서양식: western_food
        ### 기타 외국식: other_foreign_food
        ### 패스트푸드: fastfood
        ### 치킨: chicken
        ### 피자: pizza
        ### 제과제빵: baking
        ### 아이스크림/빙수: icecream
        ### 커피: coffee
        ### 음료(커피 외): drink
        ### 주점: pub
        ### 기타 외식: other eat out

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

with webdriver.Chrome(executable_path='/Users/miae/Desktop/yeardream/project/chromedriver') as driver:
    driver.get("https://franchise.ftc.go.kr/mnu/00014/program/firHope/view.do")

    search_condition_values = ['1', '2', '3'] # 업종별, 가맹본부별, 브랜드별
    type_of_business_values = ['listIndus01', 'listIndus02', 'listIndus03', 'listIndus04']
    headquarters_values = ['listHq01', 'listHq02', 'listHq03']
    brand_values = ['listBrand01', 'listBrand02', 'listBrand03']

    sel_upjong_values = ['21', '22', '23'] # 외식, 도소매, 서비스
    eat_out_values = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1'] # 외식 - 중분류
    wholesale_and_retail_values = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2'] # 도소매 - 중분류
    service_values = ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'O ', 'H3', 'I3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3', 'P3', 'Q3', 'R3', 'S3', 'T3', 'U3'] # 서비스 - 중분류

    
