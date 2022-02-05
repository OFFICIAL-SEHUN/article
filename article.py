#version 1.0.0 (22/02/06)
#version-naming : https://kiwinam.com/posts/33/version-naming/

import re
import requests
from bs4 import BeautifulSoup
keyword = input("검색:")
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
for page in range(1,6): #1~10페이지 스크래핑
    print(page)
    url = "https://www.google.com/search?q={keyword}&sxsrf=APq-WBuPFgFMSKVpQIpBDpQj5jhLOp2ySQ:1644077410752&source=lnms&tbm=nws" #바로 뉴스탭
    html = requests.get(url,headers = headers) #헤더값 추가/requests 요청
    html.raise_for_status() #값이 200이면 정상
    soup = BeautifulSoup(html.text, 'lxml') # bs로 html을 lxml로 파싱

    articles = soup.find_all("div",attrs={"data-hveid":re.compile('^CBUQAQ')})  #find : 조건에 해당되는 '첫번째' 태그를 리턴 / find_all : 조건에 해당되는 '모든' 태그를 리턴 # 정규식 사용하여 태그 찾기 # articles type: bs4.element#뉴스 :WlydOe
    for article in articles:
        link = article.find('a',attrs={'class':'WlydOe'})['href'] #링크 추출 # ＠22/02/06 기사 링크 첨부 안됌 ＠
        print(link)

        press_name = article.find('span').get_text() #언론사 이름 추출
        print(press_name)

        article_name = article.find('div',attrs={'class':'mCBkyc y355M JQe2Ld nDgy9d'}).get_text() #기사제목 추출
        print(article_name)

