"""
interarrivalsHistogram.py

Code that displays histogram of interarrival times and service times from files
interarrivals.txt and service.txt

Jashon Brown 2017
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy.random import normal

#readFile function provided by Ed
def readfile(fn):
	with open(fn) as fh:
		return [float(x) for x in fh.read().split('\n')]

		
interarrivals = readfile("interarrivals.txt")
serviceTimes = readfile("service.txt")

#Number sets how many bins(time frame per bar) are to be used 
NUMBER_OF_BINS = 8

"""
3 different graphs per data set showing standard, normalized and cumulative graphs
Draws all graphs one after the other once the previous one has been closed
"""
def drawStandardInterarrivalHistogram():
        plt.hist(interarrivals, bins=NUMBER_OF_BINS)
        plt.title("Interarrival Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

def drawNormalizedInterarrivalHistogram():
        plt.hist(interarrivals, bins=NUMBER_OF_BINS, normed=True)
        plt.title("Normalized Interarrival Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

def drawCumulativeInterarrivalHistogram():
        plt.hist(interarrivals, bins=NUMBER_OF_BINS, normed=True, cumulative=True)
        plt.title("Cumulative Interarrival Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
        
def drawStandardServiceHistogram():
        plt.hist(serviceTimes, bins=NUMBER_OF_BINS)
        plt.title("Service Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
        
def drawNormalizedServiceHistogram():
        plt.hist(serviceTimes, bins=NUMBER_OF_BINS, normed=True)
        plt.title("Normalized Service Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
        
def drawCumulativeServiceHistogram():
        plt.hist(serviceTimes, bins=NUMBER_OF_BINS, normed=True, cumulative=True)
        plt.title("Cumulative Service Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
        
def drawBothHistograms():
        plt.hist(interarrivals, bins=NUMBER_OF_BINS, normed=True, label="Interarrival Times")
        plt.hist(serviceTimes, bins=NUMBER_OF_BINS, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Service Times')
        plt.title("Interarrival and Service Times")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()

drawStandardInterarrivalHistogram()
drawNormalizedInterarrivalHistogram()
drawCumulativeInterarrivalHistogram()
drawStandardServiceHistogram()
drawNormalizedServiceHistogram()
drawCumulativeServiceHistogram()
drawBothHistograms()

