
import csv
a=[]

with open('some.csv','r') as f:
	reader=csv.reader(f,skipinitialspace=True,delimiter=',',quoting=csv.QUOTE_NONE)
	for row in reader:
		a.append(row)
	print(a)
