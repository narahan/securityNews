
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen
from bs4 import BeautifulSoup as bss

req = urlopen('https://movie.naver.com/movie/running/current.nhn')
data = req.read().decode('utf-8')
bb = bss(data, 'html.parser')
find = bb.find_all('ul', {'class':'lst_detail_t1'})
print(find)
