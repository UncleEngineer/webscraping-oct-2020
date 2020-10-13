#goldprice.py

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def GoldPrice():
	url = 'https://www.goldtraders.or.th/default.aspx'
	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')

	allclass = ['DetailPlace_uc_goldprices1_lblBLSell',
			    'DetailPlace_uc_goldprices1_lblBLBuy',
			    'DetailPlace_uc_goldprices1_lblOMSell',
			    'DetailPlace_uc_goldprices1_lblOMBuy']

	allprice = []
	for al in allclass:
		rawdata = data.find_all('span',{'id':al})
		allprice.append(float(rawdata[0].text.replace(',','')))
	#print(allprice)
	header = ['ทองคำแท่ง-ขายออก','ทองคำแท่ง-รับซื้อ','ทองรูปพรรณ-ขายออก','ทองรูปพรรณ-รับซื้อ']

	result = {}

	for h,p in zip(header,allprice):
		result[h] = p

	#print(result)
	return result

price = GoldPrice()
#print(price['ทองรูปพรรณ-รับซื้อ'])

for h,p in price.items():
	#print(h,p)
	print('{} ราคา {:,.2f} บาท'.format(h,p))

