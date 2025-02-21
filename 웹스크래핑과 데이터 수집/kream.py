from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # K 대문자입니다.

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pymysql

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
options_ = Options()
options_.add_argument(f"User-Agent={header_user}") # 유저정보 넣기
options_.add_experimental_option("detach", True) #자동으로 브라우저가 종료되지 않음
options_.add_experimental_option("excludeSwitches", ["enable-logging"])
options_.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options_)

url = "https://kream.co.kr"
driver.get(url)

#돋보기 누르기
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()

search = input("검색한 브랜드를 입력해주세요 :")
#검색어 입력 후 엔터
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(search)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(30):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.7)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner") #list 형태로 담겨요

product_list = []

for item in items:
    product_name = item.select_one(".translated_name").text

    # 제품명에 후드가 들어간것만 출력할 예정입니다.
    if "후드" in product_name: #후드가 있어 그럼 true
        category = "상의"
        product_brand = item.select_one(".product_info_brand.brand").text
        product_price = item.select_one(".text-lookup.bold.display_paragraph.line_break_by_truncating_tail").text

        product = [category, product_brand, product_name, product_price]
        product_list.append(product)

        #list 형태로 담고 싶은데  [["상의", "슈프림", "티니핑 콜라보 후드", "323220000"], ["상의", "슈프림", "파머핑 콜라보 후드", "10023220000"]]
        print(f"카테고리 : {category}")
        print(f"브랜드 : {product_brand}")
        print(f"제품명 : {product_name}")
        print(f"가격 : {product_price}")
        print()
    
    driver.quit()

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd ='8715',
    db = 'kream',
    charset='utf8mb4'
)

connection.cursor()
#함수
def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ()) #쿼리문을 담아서 데이터베이스 보냄
        if query.strip().upper().startswith('select'):
            return cursor.fetchall() #접속한 db에 모든 정보 가져오고
        else :
            connection.commit()

for i in product_list :
    execute_query(connection, "INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0], i[1], i[2], i[3]))