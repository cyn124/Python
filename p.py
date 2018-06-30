import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []
k=[]
t=[]

infile= open('summary.PRES','r')
while True:
	theline=infile.readline()
	x.append(theline[4:12])
	y.append(theline[15:21])
	if len(theline)==0:
                break
infile.close()

for i in x:
	j=i.replace(' ','')
	k.append(j)
k.remove('')
k=[float(z) for z in k]

for u in y:
	p=u.replace(' ','')
	t.append(p)
t.remove('')
t=[float(q) for q in t]

plt.plot(k,t)
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Pressure versus Time')
plt.show()
