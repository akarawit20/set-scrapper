from lxml import html
import requests
import numpy as np
import time


def scrap_companyhighlight(stock_symbol):
	url = "https://www.settrade.com/C04_03_stock_companyhighlight_p1.jsp?txtSymbol=" + stock_symbol + "&ssoPageId=12&selectPage=3"
	page_source = requests.get(url)
	tree = html.fromstring(page_source.content)

	filteted_element = tree.xpath('//div[@class="col-xs-8 col-md-6 text-left"]')

	industry = np.asarray(list(map(lambda text: text.text, filteted_element)))[2]

	return [industry]


def scrap_financial(stock_symbol):
	url = "https://www.settrade.com/C04_06_stock_financial_p1.jsp?txtSymbol=" + stock_symbol + "&ssoPageId=13&selectPage=6"
	page_source = requests.get(url)
	tree = html.fromstring(page_source.content)

	td_elements = tree.xpath('//td')

	table_1d = np.asarray(list(map(lambda quote: quote.text, td_elements))[2:44])
	table_1d = np.asarray(list(map(lambda quote: quote.replace("\xa0\xa0", "" ), table_1d)))

	table_2d = np.reshape(table_1d, (7, 6))[:, :-1]

	return extract_uptodate(table_2d)


def extract_uptodate(quote):
	quote_present = list(map(lambda price: float(price.replace(',','')), quote.T[1]))

	return quote_present


if __name__ == '__main__':
	stock_symbols = ['AOT', 'BDMS']
	all_stock_data = []
	for stock_symbol in stock_symbols:
	    try:
	        stock_data = [stock_symbol] + scrap_companyhighlight(stock_symbol) + scrap_financial(stock_symbol)
	        print(stock_data)
	        all_stock_data.append(stock_data)
	    except:
	        pass
	    time.sleep(0.5)



