
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss


# 모든 https 통신은 필요한 인증서와 호스트명을 기본적으로 체크하게 됨
# 영향 받는 라이브러리는 urllib, urllib2, http, httplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Boannews Base URL
base_url ='https://www.boannews.com'

#url = base_url + '/media/list.asp?mkind=1'
url = base_url + '/search/news_list.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED'
#https://www.boannews.com/search/news_list.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED

f = urlopen(url)
b = f.read()
soup = bss(b, 'html.parser')





divs = soup.find_all('div', { 'class': 'news_list' })


file_data = []
def getBoanData():
	num = 0
	for i in divs:

		f = {}
		title = i.find_all('span', {'class': 'news_txt'})
		title = i.find_all('span')[0]
		title = title.string

		url = i.find('a')['href']
		url = base_url + url

		date = i.find_all('span', {'class': 'news_writer'})
		# ex) <span class="news_writer">권준  기자 | 2019.08.12 12:02</span>

		date = i.find_all('span')[1]
		# ex) 2019.08.12 12:02
		date = date.string.partition('|')[2]
		# ex) 2019.08.12
		date = date.split(' ')[1]

		num = num + 1
		f['num'] = num
		f['date'] = date
		f['title'] = title
		f['url'] = url
		

		file_data.append(f)
		
	return file_data





