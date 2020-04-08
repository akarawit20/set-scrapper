from sklearn.cluster import DBSCAN
import numpy as np
import csv

with open('all_stock_data.csv', newline='') as f:
	reader = csv.reader(f)
	all_stock_data = np.asarray(list(reader))

print('clustering...')
clustering = DBSCAN(eps=5, min_samples=2).fit(all_stock_data[:, 2:])

print(clustering.labels_)

out = clustering.labels_

for n in range(len(out)):
	if out[n] == 0:
		print(n+1, all_stock_data[n])