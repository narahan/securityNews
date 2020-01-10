
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss


# 모든 https 통신은 필요한 인증서와 호스트명을 기본적으로 체크하게 됨
# 영향 받는 라이브러리는 urllib, urllib2, http, httplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Boannews Base URL
base_url = 'https://www.boannews.com/'
base_url2 = base_url + 'media/list.asp?mkind=1'
	   # ='https://www.boannews.com/media/list.asp?mkind=1'
# https://www.boannews.com/media/view.asp?idx=85674


# url = base_url + 'idx=85674'
# url = base_url + 'view.asp?idx='
# url = 'https://www.boannews.com/media/view.asp?idx='



f = urlopen(base_url2)
b = f.read()
soup = bss(b, 'html.parser')



# divs = soup.find_all('div', { 'id': 'news_area' })
divs = soup.find_all('div', {'class' : 'news_list'})

# divs = soup.find_all('div', { 'class': 'news_main_title' })



# To Do!!!
# title, url, number 가져오기




file_data = []
def getBoanData():
	num = 0
	for i in divs:
		f = {}
		# title = i.find_all('span', {'class' : 'news_txt'})
		title = i.find_all('span')[0]
		title = title.string

		# /media/view.asp?idx=85672&page=1&mkind=1&kind=2
		url = i.find('a')['href']

		url = base_url + url

		num = num + 1
        
#         뉴스 작성 날짜 노출 결정하기
		f['num'] = num
		f['title'] = title
		f['url'] = url
		
		file_data.append(f)
		
	return file_data
    

getBoanData()




# file_data = []
# def getBoanData():
# 	num = 0
# 	for i in divs:

# 		f = {}
# 		title = i.find_all('span', {'class': 'news_txt'})
# 		title = i.find_all('span')[0]
# 		title = title.string

# 		url = i.find('a')['href']
# 		url = base_url + url

# 		date = i.find_all('span', {'class': 'news_writer'})
# 		# ex) <span class="news_writer">권준  기자 | 2019.08.12 12:02</span>

# 		date = i.find_all('span')[1]
# 		# ex) 2019.08.12 12:02
# 		date = date.string.partition('|')[2]
# 		# ex) 2019.08.12
# 		date = date.split(' ')[1]

# 		num = num + 1
# 		f['num'] = num
# 		f['date'] = date
# 		f['title'] = title
# 		f['url'] = url
		

# 		file_data.append(f)
		
# #	return file_data
# 	print(file_data)

# getBoanData()



