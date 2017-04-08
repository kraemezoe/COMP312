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

# if there aren't enough arguments
if len(sys.argv)<2:
	print "Usage: python %s <data filename>" % sys.argv[0]
	sys.exit()

# read data
fn = sys.argv[1]
fh = open(sys.argv[1])
fd = fh.read().split('\n')[4:-1]
fd = [x.split('  ') for x in fd]

# in case this file was recorded on a windows machine, we need to strip all \r
fd = [[x[0],x[1].split('\r')[0]] for x in fd]
print fd

# net customers in system
customers = 0
time = [float(fd[0][0])]
net_customers = [0]
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
interarrivals = \
	[float(i[0])-float(j[0]) for i,j in zip(arrivals,[fd[4]]+arrivals[:-1])]
interarrival = sum(interarrivals)/len(interarrivals)

# service time - harder to do
stime = []
lastc = 0
last_time = 0
for c,t in zip(net_customers,time):
	if c-lastc<0:
		if last_time!=0:
			if c>0:
				stime.append((t-last_time)/2)
			else:
				stime.append(t-last_time)	
		last_time = t
	
	lastc = c
stime = sum(stime)/len(stime)

# print stats
print "Interarrival time: %f seconds" % interarrival
print "Interarrival rate: %f per minute" % (interarrival**-1*60)
print "Service time: %f seconds" % stime
print "Service rate: %f per minute" % (stime**-1*60)
print "C*Service rate: %f per minute" % (stime**-1*60*2)
print "Converges? %s" % ('yes' if (interarrival**-1*60)/(stime**-1*60*2)<1 else 'false')


# change times to 24 hour
time = [x/60/60 for x in time]

# show graph		
plt.step(time,net_customers)
plt.show()
