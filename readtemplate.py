"""
readtemplate.py

Some code that reads in the interarrival/service times

COMP489
Ed Haslam 2017
"""

def readfile(fn):
	with open(fn) as fh:
		return [float(x) for x in fh.read().split('\n')]

# for example...		
print readfile("interarrivals.txt")
