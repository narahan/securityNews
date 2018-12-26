
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
 

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Boannews Base URL
base_url =' https://www.boannews.com'


url = base_url + '/media/list.asp?mkind=1'

f = urlopen(url)
b = f.read()
soup = bss(b, 'html.parser')

divs = soup.find_all('div',{'class': 'news_list'})

print('==============================================')


try:
	# get title, url list
	for i in divs:
		#titleArr = i.find_all('span', {'class': 'news_txt'})
		titleArr = i.find_all('span')[0]
		print(titleArr.string)

		urlArr = i.find('a')['href']
		print(base_url + urlArr)
# test	
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.reason)
	print(e.headers)
