import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []


infile= open('summary.TEMP','r')

while True:
	theline=infile.readline()
	for i, line in enumerate(infile):
		if i==1:
			x.append(float(theline[7:12]))
			y.append(float(theline[19:23]))
	if len(theline)==0:
                break

#s=csv.writer(open('e.csv','wb'), delimiter=' ', 
	
#str1=''.join(x)
#str1.replace(' ','_')
#print (str1)
#	print (x)
#	y.replace(' ','0')
#	print (y)

#	if len(theline)==0:
#		break

infile.close()




plt.plot(x,y)

plt.xlabel('time')
plt.ylabel('temperature')
plt.title('Temperature vs Time')
plt.axis([0,1000,0,300])
plt.show()
