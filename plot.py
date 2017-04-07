"""
plot.py
I made this to display stats from our files
COMP489
Ed Haslam 2017
"""

import sys
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt

# read data
fn = sys.argv[1]
fh = open(sys.argv[1])
fd = fh.read().split('\n')[4:-1]
fd = [x.split('  ') for x in fd]


# net customers in system
customers = 0
time = []
net_customers = []
for rec in fd:
	if rec[1] == 'a':
		customers += 1
		net_customers.append(customers)
		time.append(float(rec[0]))
	elif rec[1] == 'd':
		if customers == 0:
			continue
		customers -= 1
		net_customers.append(customers)
		time.append(float(rec[0]))
	elif rec[1] == 'empty':
		customers = 0
	elif rec[1] == 'reset':
		customers = 0

# interarrival time
arrivals = filter(lambda x: x[1]=='a',fd)
interarrivals = 
	[float(i[0])-float(j[0]) for i,j in zip(arrivals,[fd[4]]+arrivals[:-1])]
interarrival = sum(interarrivals)/len(interarrivals)

# service time - harder to do

# print stats
print "Interarrival time: %f seconds, I presume" % interarrival

# show graph		
plt.step(np.array(time),np.array(net_customers))
plt.show()
