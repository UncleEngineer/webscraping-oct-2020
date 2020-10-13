from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def CheckPrice(CODE):
	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(CODE)
	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')

	# class = col-xs-6
	rawdata = data.find_all('div',{'class':'col-xs-6'})
	#print('COUNT',len(rawdata))
	price = rawdata[2].text
	#print('Price:', price)
	update = data.find_all('span',{'class':'stt-remark'})

	#print(update[0].text)
	update = update[0].text[13:]

	text = 'STOCK: {} PRICE: {} BAHT UPDATE: {}'.format(CODE,price,update)
	#print(text)
	return (text,float(price))


code = 'AOT'
quantity = 100
txt,price = CheckPrice(code)
cal = price * quantity
#print(type(cal))
print('หุ้น: {} จำนวน {} หุ้น ราคา: {:,.0f} บาท'.format(code,quantity,cal))
print(txt)


