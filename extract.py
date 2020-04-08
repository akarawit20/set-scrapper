import pickle
import numpy as np

pickle_in = open('all_stock_data.p', 'rb')
all_stock_data = pickle.load(pickle_in)


def get_from_summary(stock_data, column_name):
	#from latest data
	#use for summary
	summary_table = stock_data[7].values
	location = np.where(summary_table[0]==column_name)
	value = summary_table[1][location[0]]
	return float(value)


def get_from_table(stock_data, table_name, row_name, year=1): #last year=1, last2 year=2
	#use for all table but summary
	for table in stock_data:
		if table[0][0] == table_name:
			value = table.loc[table[0] == row_name].values[0][1]
			return float(value)



def altman_z_scores_calculator(stock_data, year=1):

	#calculate derivatives
	total_assets = get_from_table(stock_data, 'Statement of Financial Position (MB.)', 'Total Assets', year)
	return total_assets
	working_capital = get_from_table(stock_data, 'Statement of Financial Position (MB.)', 'Total Assets', year) - get_from_table(stock_data, 'Statement of Financial Position (MB.)', 'Total Liabilities', year)
	retained_earnings = get_from_table(stock_data, 'Statement of Financial Position (MB.)', 'Retained Earnings (Deficit)', year)
	earning_before_interest_and_taxes = get_from_table(stock_data, 'Statement of Comprehensive Income (MB.)', 'EBIT', year)
	market_value_of_equity = get_from_summary(stock_data, 'Market Cap (MB.)')
	sales = get_from_table(stock_data, 'Statement of Comprehensive Income (MB.)', 'Total Revenues', year)


	#calculate intermediates
	x1 = working_capital/total_assets
	x2 = retained_earnings/total_assets
	x3 = earning_before_interest_and_taxes/total_assets
	x4 = market_value_of_equity/total_assets
	x5 = sales/total_assets

	#calculate scores
	z_score_original = 1.2*x1 + 1.4*x2 + 3.3*x3 + 0.6*x4 + 1.0*x5
	z_score_bankruptcy_model_non_manufacturers = 6.56*x1 + 3.26*x2 + 6.72*x3 + 1.05*x4
	z_score_emerging_market = 3.25 + 6.56*x1 + 3.26*x2 + 6.72*x3 + 1.05*x4

	return [z_score_original, z_score_bankruptcy_model_non_manufacturers, z_score_emerging_market]




#export csv file of data wanted
export_table = []

#list all symbols
all_stock_symbol = list(all_stock_data)

result = [0,0]

for stock_symbol in all_stock_symbol:
	try:
		altman_z_scores = altman_z_scores_calculator(stock_symbol)
		export_table.append(altman_z_scores)
		result[0] += 1
	except Exception as e:
		print(stock_symbol, e)
		result[1]+=1



#output
export_table = np.asarray(export_table)
print(export_table)

print(result)


















