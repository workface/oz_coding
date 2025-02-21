import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

soup = BeautifulSoup(req.text, "html.parser")

#print(soup)

top50 = soup.select('#lst50 > td > div')    # 공통적인 부분이 #lst50 > td:nth-child(6) > div 이기때문에 이것을 묶은 리스트를 만들어서 for문
top100 = soup.select('#lst100 > td > div')
# for i in top50 :
#     rank = i.select_one('span.rank')
#     title = i.select('div > div.ellipsis.rank01 > span > a')

#     print(rank, title)



# for i in top50 :
#     rank = i.select_one('span.rank')

#     if rank is not None :
#         print(rank.text, end = ' ')
    
#     title = i.select_one('div > div.ellipsis.rank01 > span > a')

#     if title is not None :
#         singer = i.select_one('div.ellipsis.rank02 > a')
#         print(title.text, '-', singer)

top50 = soup.select('#lst50 > td > div') 
top100 = soup.select('#lst100 > td > div')    
top1_100 = top50 + top100    

for i in top1_100 :
    rank = i.select_one('span.rank')

    if rank is not None :
        print(rank.text, end = '. ')
    
    title = i.select_one('div > div.ellipsis.rank01 > span > a')

    if title is not None :
        singer = i.select_one('div.ellipsis.rank02 > a').text
        print(singer, '-', title.text)



#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a    <<< 1위 노래 title 셀렉트 
#lst100 > td:nth-child(2) > div > span.rank                              <<< 1위 노래 행킹
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a            <<< 1위 노래 가수 셀렉트
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a     <<<<< 2위 노래 title 셀렉트
#lst50 > td:nth-child(2) > div > span.rank
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a            <<<<2위 노래 가수 셀렉트

#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a      <<<<<51위 노래 제목
#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a                 <<<<< 51위 노래 가수
#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a         <<<< 52위 노래 제목
#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a             <<<< 52위 노래 제목


#lst100 > td:nth-child(2) > div > span.rank


# 참고 코드 : https://chaeyami.tistory.com/12