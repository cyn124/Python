import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []
k=[]
t=[]

infile= open('summary.ETOT','r')
while True:
	theline=infile.readline()
	if (theline[23:29] !=""):
		x.append(theline[4:12])
		y.append(theline[17:29])
	if len(theline)==0:
       	        break
infile.close()

for i in x:
	j=i.replace(' ','')
	k.append(j)
k=[float(z) for z in k]

for u in y:
	p=u.replace(' ','')
	t.append(p)

t=[float(q) for q in t]

plt.plot(k,t)
plt.xlabel('Time')
plt.ylabel('Total Energy')
plt.title('Total Energy versus Time')
plt.show()
