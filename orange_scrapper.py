import requests
import pandas as pd
import time


def scrap_all_table(stock_symbol):
	url = 'https://www.set.or.th/set/factsheet.do?symbol='+stock_symbol+'&ssoPageId=3&language=en&country=TH'
	page_source = requests.get(url)
	tables = pd.read_html(page_source.text)

	return tables


if __name__ == '__main__':
	stock_symbols = ['BTS']
	all_stock_data = []
	for stock_symbol in stock_symbols:
		try:
			stock_data = scrap_all_table(stock_symbol)
			all_stock_data.append(stock_data)
			print(stock_data)
		except:
			pass
		time.sleep(0.5)


