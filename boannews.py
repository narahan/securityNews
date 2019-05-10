


from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
from sqlite3 import connect

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


con = connect('news.db')
cur = con.cursor()

table = 'create table boannews(boannews text, title text, url text);'
cur.execute(table)


divs = soup.find_all('div',{'class': 'news_list'})

# get title, url list
for i in divs:
	titleArr = i.find_all('span', {'class': 'news_txt'})
	titleArr = i.find_all('span')[0]
	titleArr = titleArr.string

	urlArr = i.find('a')['href']
	urlArr = base_url + urlArr
	companyText = 'boannews'

	t = (companyText, titleArr, urlArr)
	cur.execute('insert into boannews values (?,?,?)', t)
	print(t)

con.commit()
con.close()

