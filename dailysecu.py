


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




divs = soup.find_all('div',{'class': 'box'})


# get title, url list
for i in divs:
	titleArr = i.find('a', {'class' : 'title_a'})
	print(titleArr.string)	

	urlArr = i.find('a')['href']
	print(base_url + urlArr)



