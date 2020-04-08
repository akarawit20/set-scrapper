import requests
from lxml import html


def get_stock_symbols():
	url = "http://siamchart.com/stock/"
	page_source = requests.get(url)
	tree = html.fromstring(page_source.text)
	filtered_elements = tree.xpath('//a/text()')[19:]

	stock_fullname = list(map(lambda name:name, filtered_elements))
	stock_symbols = list(map(lambda name:name[:name.find('(')], stock_fullname))

	return stock_symbols


if __name__ == '__main__':
	print(get_stock_symbols())


