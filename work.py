import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('some.csv','w') as f:
	
	infile= open('summary.TEMP','r')

	while True:
		theline=infile.readline()
		writer=csv.writer(f)
       		writer.writerows(theline[5:12])

	#	x.append(theline[5:12])
	#	y.append(theline[18:23])
		if len(theline)==0:
        	        break



#str1=''.join(x)
#str1.replace(' ','_')
#print (str1)
#	print (x)
#	y.replace(' ','0')
#	print (y)

#	if len(theline)==0:
#		break

infile.close()




#plt.plot(x,y)

plt.xlabel('time')
plt.ylabel('temperature')
plt.title('Temperature vs Time')
plt.axis([0,1000,0,300])
plt.show()
