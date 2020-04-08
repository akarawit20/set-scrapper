import time
import pickle

import black_scrapper
import orange_scrapper


all_stock_data = {} # <-dict containing lists
stock_symbols = black_scrapper.get_stock_symbols()
#stock_symbols = ['PTT', 'AOT', 'BTS', 'BH'] #for fast testing
for stock_symbol in stock_symbols:
	try: #<-- check if data still available
		tables = orange_scrapper.scrap_all_table(stock_symbol)
		all_stock_data[str(stock_symbol)] = tables

		print(stock_symbol, 'scrapping successful')
		time.sleep(0.5)
	except:
		print(stock_symbol, 'scrapping FAILED!!! ---------- stock symbol not found')
		time.sleep(0.5)
		pass



pickle_out = open('all_stock_data.p', 'wb')
pickle.dump(all_stock_data, pickle_out)
pickle_out.close()


'''
example
all_stock_data['PTT']['financial_position']['Cash'][1]
>>> 292542.46
'''





