#version 1.0.1 (22/02/08)
#version-naming : https://kiwinam.com/posts/33/version-naming/

import re
import requests
from bs4 import BeautifulSoup
keyword = input("검색:")
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
page = 0
cnt = 0
for i in range(0,60,10): #1~5페이지 스크래핑
    page += 1
    print(page)
    url = "https://www.google.com/search?q={0}&tbm=nws&start={1}".format(keyword,i) #바로 뉴스탭 + 다음 페이지
    html = requests.get(url,headers = headers) #헤더값 추가/requests 요청
    html.raise_for_status() #값이 200이면 정상
    soup = BeautifulSoup(html.text, 'lxml') # bs로 html을 lxml로 파싱
    
    articles = soup.find("div",attrs={"class":'v7W49e'}) #태그 찾기
    ariticles = articles.find_all("div") # 다시 articles에서 div 태그 찾기
    
    for article in articles:
        link = article.find('a',attrs={'class':'WlydOe'})['href'] #링크 추출 
        print(link)
    
        press_name = article.find('span').get_text() #언론사 이름 추출
        print(press_name)
    
        article_name = article.find('div',attrs={'class':'mCBkyc y355M JQe2Ld nDgy9d'}).get_text() #기사제목 추출
        print(article_name)
        print("----------------------------------------")
        cnt += 1
    
print(cnt,"개의 기사 검색")
