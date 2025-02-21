import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색할 키워드를 입력해 주세요 : ")

url = base_url + keyword

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") #select 해당하는 모든 정보를 가져옵니다. select_one 해당하는 것 중에서 가장 위에있는 하나만 가져옵니다.

rank = 1
    
for i in results :
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
    rank += 1
    
# print(results)


