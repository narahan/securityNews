
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
 

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

base_url =' https://www.boannews.com'


url = base_url + '/media/list.asp?mkind=1'

# base url



f = urlopen(url)
b = f.read()
soup = bss(b, 'html.parser')

#main = soup.find_all('div', {'id': 'news_area'})




divs = soup.find_all('div',{'class': 'news_list'})

print('==============================================')
#print(divs)


# get title list
for i in divs:
	titleArr = i.find_all('span', {'class': 'news_txt'})
	#print(titleArr)

# get href lis
for j in divs:
	aa = j.find('a')['href']
	print(base_url + aa)


