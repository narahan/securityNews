

from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
import json
import os
from collections import OrderedDict
 



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


def getData():
	num = 0
	for i in divs:
		f = {}

		titleArr = i.find_all('span', {'class': 'news_txt'})
		titleArr = i.find_all('span')[0]
		titleArr = titleArr.string

		urlArr = i.find('a')['href']
		urlArr = base_url + urlArr

		dateArr = i.find_all('span', {'class': 'news_writer'})
		# ex) <span class="news_writer">권준  기자 | 2019.08.12 12:02</span>

		dateArr = i.find_all('span')[1]
		# ex) 2019.08.12 12:02
		dateArr = dateArr.string.partition('|')[2]
		# ex) 2019.08.12
		dateArr = dateArr.split(' ')[1]

		num = num + 1
		f['num'] = num
		f['date'] = dateArr
		f['title'] = titleArr
		f['url'] = urlArr

		file_data.append(f)

	return file_data



# for i in divs:
# 	num = num + 1
# 	print(num)



