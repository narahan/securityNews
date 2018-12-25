
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss
 

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.boannews.com/media/list.asp?mkind=1'
f = urlopen(url)
b = f.read()
soup = bss(b, 'html.parser')
divs = soup.find_all('div',{'class': 'news_main_title'})


print('==============================================')

print(divs)
