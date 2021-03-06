from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
                                        StaleElementReferenceException
import pymongo
import time
from multiprocessing import Pool


def land_crawling(item):
    options = webdriver.FirefoxOptions()
    options.headless = True

    # mongodb에서 상권 좌표 가져오기
    connection = pymongo.MongoClient("mongodb+srv://user1:uZGuuMyRngM3izgG@cluster0.cu0c3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = connection.get_database("elice")
    collection2 = db.get_collection("real_estate")

    naver_land = "http://new.land.naver.com/offices?"

    if list(collection2.find({'상권_코드':item["상권_코드"]})):
        print(f"{item['상권_코드']} skip")
        return
    # 상권 좌표로 검색한 페이지에서 크롤링
    with webdriver.Firefox(options=options) as driver:
        driver.implicitly_wait(10)
        print("**********************************************************")
        print(item['상권_코드'], item['상권_코드_명'], item['위도'], item['경도'])
        latitude, longitude = item['위도'], item['경도']
        driver.get(f"{naver_land}ms={latitude},{longitude}&a=SG&e=RETAIL")
        # # 상가 매물 리스트 스크롤 끝까지 내리기
        SCROLL_PAUSE_SEC = 2
        building_list = driver.find_element_by_xpath(
            '//*[@id="listContents1"]/div'
            )
        last_height = driver.execute_script(
            'return arguments[0].scrollHeight',
            building_list
            )
        while last_height < 5000:
            driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight',
                building_list
                )
            time.sleep(SCROLL_PAUSE_SEC)
            new_height = driver.execute_script(
                'return arguments[0].scrollHeight',
                building_list
                )
            if new_height == last_height:
                time.sleep(SCROLL_PAUSE_SEC)
                if new_height == last_height:
                    break
            last_height = new_height
        print("화면 높이 :", last_height)
        # 다 내린 후에는 하나씩 클릭해서 정보 읽어오기
        link_list = driver.find_elements_by_xpath(
            '//*[@id="listContents1"]//a[@class="item_link"]'
            )
        data = []
        for i in range(len(link_list)):
            if i > 50:
                break
            title = link_list[i].find_element_by_xpath('div[1]/span')
            bill_type_list = link_list[i].find_element_by_xpath(
                'div[2]/span[1]'
                )
            bill_amount_list = link_list[i].find_element_by_xpath(
                'div[2]/span[2]'
                )
            info = {}
            info['상권_코드'] = item['상권_코드']
            info['분류'] = title.text
            info['거래방식'] = bill_type_list.text
            info['가격'] = bill_amount_list.text
            link_list[i].click()
            try:
                table = driver.find_element_by_xpath(
                    '//*[@id="detailContents1"]/div[1]/table/tbody'
                    )
                keys = table.find_elements_by_tag_name('th')
                values = table.find_elements_by_tag_name('td')
                for key, value in zip(keys, values):
                    if key.text not in ['매물설명']:
                        info[key.text] = value.text
                if info:
                    data.append(info)
            except NoSuchElementException or \
                    StaleElementReferenceException:
                time.sleep(3)
                try:
                    table = driver.find_element_by_xpath(
                        '//*[@id="detailContents1"]/div[1]/table/tbody'
                        )
                    keys = table.find_elements_by_tag_name('th')
                    values = table.find_elements_by_tag_name('td')
                    for key, value in zip(keys, values):
                        if key.text not in ['매물설명']:
                            info[key.text] = value.text
                    if info:
                        data.append(info)
                except NoSuchElementException or \
                        StaleElementReferenceException:
                    print('Can\'t load element')
            print(info.get('매물번호'))
        print("링크 수:", len(link_list))
        print("생성된 데이터:", len(data))
        # mongodb에 적재
        if data:
            collection2.insert_many(data)
        driver.quit()


if __name__ == '__main__':
    connection = pymongo.MongoClient("mongodb+srv://user1:uZGuuMyRngM3izgG@cluster0.cu0c3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = connection.get_database("elice")
    collection = db.get_collection("area_info")
    collection2 = db.get_collection("real_estate")

    # collection2.delete_many({})
    items = list(collection.find())

    pool = Pool(processes=1)  # 멀티 프로세스 시 오히려 느려짐
    pool.map(land_crawling, items)
