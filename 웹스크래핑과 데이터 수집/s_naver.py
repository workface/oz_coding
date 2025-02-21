from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import  time

header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색할 키워드를 입력해 주세요 : ")

options_ = Options()
options_.add_argument(f"User-Agent={header}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])
options_.add_experimental_option("excludeSwitches", ["enable-automation"])

url = base_url + keyword
driver = webdriver.Chrome(options=options_)
driver.get(url)

for i in range(5) :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)




html = driver.page_source
soup = BeautifulSoup(html)
results = soup.select(".view_wrap")

for rank, i in enumerate(results, 1) :
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")['href']
    writer = i.select_one(".name").text
    dsc = i.select_one(".dsc_link").text

    print(f"{rank}번째 블로그 글") #n번째 블로그 글
    print(f'제목 : {title}')
    print(f'링크 : {link}')
    print(f'작성자 : {writer}')
    print(f'글요약 : {dsc}')
    print("")

driver.quit()
