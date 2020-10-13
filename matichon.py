#goldprice.py

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def News(cat='economy'):
	url = 'https://www.matichon.co.th/{}'.format(cat)
	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')

	news = data.find_all('h3',{'class':'entry-title td-module-title'})
	news = news[:12]

	topics = []

	for n in news:
		dt = [n.a['title'],n.a['href']]
		topics.append(dt)

	#title = news[0]
	#print(title.a['title'])
	#print(title.a['href'])
	#print(len(news))

	print(topics)
	return topics

data = News()

for d in data:
	print(d[1])
	print('-----')