#키워드 속의 키워드 함수 구현

import requests
from bs4 import BeautifulSoup

keyword = input("keyword : ")
i = input("page : ")

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
url = "https://www.google.com/search?q={0}&tbm=nws&start={1}".format(keyword,i*10)
html = requests.get(url,headers=headers) 
html.raise_for_status()
soup = BeautifulSoup(html.text, 'lxml')

articles = soup.find("div",attrs={"class":'v7W49e'}) #기사 전체

banners_body = articles.find('g-section-with-header',attrs={'class':'yG4QQe TBC9ub'}) #기사 전체에서 배너만 찾기 
cnt = 0
if banners_body: #배너 뉴스 여부 
    banner_in_article = banners_body.find_all('div',attrs={'class':'JJZKK yLWA8b'}) # 배너뉴스 안 기사 3개
    for banner in banner_in_article :
        banner_nws_link = banner.find('a',attrs={'class':'WlydOe'})['href']
        print(banner_nws_link)
        banner_press_name = banner.find('div',attrs={'class':'CEMjEf NUnG9d'}).get_text()
        print(banner_press_name)
        banner_article_name = banner.find('div',attrs={'class':'mCBkyc y355M nDgy9d'}).get_text() #기사제목 추출
        print(banner_article_name)
        print("-"*30)
        cnt+=1
# 문제점 : g-section을 찾고 출력하고 다음 g-section을 찾아야함
#           + g-section 찾고도 하나의 g-section에서 기사 세개 뽑아야함

print(cnt)       

'''
def banner_nws():
    articles = soup.find("div",attrs={"class":'v7W49e'}) #기사 전체
    banners_body = articles.find('g-section-with-header',attrs={'class':'yG4QQe TBC9ub'}) #기사 전체에서 배너만 찾기 
    banner_in_3 = banners_body.find_all('div',attrs={'class':'JJZKK yLWA8b'}) # 배너뉴스 안 기사 3개
    if banners_body: #배너 뉴스 여부
        for banner in banner_in_3 :
            banner_nws_link = banner.find('a',attrs={'class':'WlydOe'})['href']
            print(banner_nws_link)
            banner_press_name = banner.find('div',attrs={'class':'CEMjEf NUnG9d'}).get_text()
            print(banner_press_name)
            banner_article_name = banner.find('div',attrs={'class':'mCBkyc y355M JQe2Ld nDgy9d'}).get_text() #기사제목 추출
            print(banner_article_name)
            '''