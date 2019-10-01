


from urllib.request import urlopen
from bs4 import BeautifulSoup as bss



# 모든 https 통신은 필요한 인증서와 호스트명을 기본적으로 체크하게 됨
# 영향 받는 라이브러리는 urllib, urllib2, http, httplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



# Boannews Base URL
base_url ='https://www.dailysecu.com'
url = base_url + '/?mod=news&act=articleList&view_type=S&sc_code=1435901200'
# url open 
f = urlopen(url)


# page read
b = f.read()
soup = bss(b, 'html.parser')



divs = soup.find_all('div',{'class': 'list-block'})

file_data = []

def getDailyData():
	num = 0
	for i in divs:


		f = {}
		titleArr = i.find('div', {'class' : 'list-titles'})
		titleArr = titleArr.string
		

		urlArr = i.find('a')['href']
		urlArr = base_url + urlArr

		# ex) <span class="list-dated">이슈 | 길민권  기자 | 2019.08.12 12:02</span>
		dateArr = i.find_all('div', {'class': 'list-dated'})[0]
		dateArr = dateArr.string
		dateArr = dateArr.string.partition('|')[2]
		dateArr = dateArr.partition('|')[2]
		# ex) 2019.08.12 12:02
		dateArr = dateArr.split(' ')[1]

		
		num = num + 1
		f['num'] = num 
		f['date'] = dateArr
		f['title'] = titleArr
		f['url'] = urlArr

		file_data.append(f)
	return file_data





