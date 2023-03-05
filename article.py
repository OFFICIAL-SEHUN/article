#version 2.0.0 (22/02/20)
import requests
from bs4 import BeautifulSoup
keyword = input("keyword : ")
i = input("page : ")
text1,text2 = input("text1, text2 : ").split()
def crawler(keyword,i):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    n2_lst = []
    
    url = "https://www.google.com/search?q={0}&tbm=nws&start={1}".format(keyword,i*10) #바로 뉴스탭 + 다음 페이지
    html = requests.get(url,headers = headers) #헤더값 추가/requests 요청
    html.raise_for_status() #값이 200이면 정상
    soup = BeautifulSoup(html.text, 'lxml') # bs로 html을 lxml로 파싱
        
    articles = soup.find("div",attrs={"class":'v7W49e'}) #태그 찾기
    s= articles.find('g-section-with-header',attrs={'class':'yG4QQe TBC9ub'}) #기사 전체에서 배너만 찾기 
    for article in articles:
        
        if articles.find('g-section-with-header',attrs={'class':'yG4QQe TBC9ub'}): #기사 전체에서 배너만 찾기 
            for banner in s :
                banner_nws_link = banner.find('a',attrs={'class':'WlydOe'})['href']
                print(banner_nws_link)
                banner_press_name = banner.find('div',attrs={'class':'CEMjEf NUnG9d'}).get_text()
                print(banner_press_name)
                banner_article_name = banner.find('div',attrs={'class':'mCBkyc y355M nDgy9d'}).get_text() #기사제목 추출
                print(banner_article_name)
                print("-"*30)
            
        else:
            link = article.find('a',attrs={'class':'WlydOe'})['href'] #링크 추출 
            n2_lst.append(link)
            press_name = article.find('span').get_text() #언론사 이름 추출
            n2_lst.append(press_name)
            article_name = article.find('div',attrs={'class':'mCBkyc y355M JQe2Ld nDgy9d'}).get_text() #기사제목 추출
            n2_lst.append(article_name)

    return n2_lst
def keyword_overlap_cnt():
    keyword_lst = []
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url = "https://www.google.com/search?q=intitle%3A{0}+intext%3A{1}+{2}&tbm=nws".format(keyword,text1,text2) #바로 뉴스탭 + 다음 페이지
    html = requests.get(url,headers=headers) #requests 요청
    html.raise_for_status() #값이 200이면 정상
    soup = BeautifulSoup(html.text, 'lxml') # bs로 html을 lxml로 파싱
    articles = soup.find("div",attrs={"class":'v7W49e'}) #태그 찾기
    for article in articles:
        link = article.find('a',attrs={'class':'WlydOe'})['href'] #링크 추출 
        keyword_lst.append(link)
        press_name = article.find('span').get_text() #언론사 이름 추출
        keyword_lst.append(press_name)
        article_name = article.find('div',attrs={'class':'mCBkyc y355M JQe2Ld nDgy9d'}).get_text() #기사제목 추출
        keyword_lst.append(article_name)
    cnt = soup.find('div',attrs={'id':'result-stats'}).get_text() # 카운트
    return cnt,keyword_lst

print(crawler(keyword,i))

