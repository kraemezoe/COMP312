"""
estimates the parameter values of the exponential, erlang, and gamma
distributions using method of moments

Usage: python methodofmoments.py <interarrival/service times filename>
"""

import sys
import numpy

def moment1(fn):
	with open(fn) as fh:
		return numpy.mean([float(x) for x in fh.read().split('\n')])

def moment2(fn):
	with open(fn) as fh:
		return numpy.mean([float(x)**2 for x in fh.read().split('\n')])
def expMOM(m1):
        print 'Exponential: lambda =', 1/m1

def ereMOM(m1, m2):
        var =  m2-(m1**2)
        mu = m1/var
        k = m1*mu
        print 'Erlang: k =',k,'mu =',mu 

def gammaMOM(m1, m2):
        var = m2-(m1**2)
        theta = m1/var
        k = m1/theta
        print 'Gamma: k =',k,'theta =',theta

readFrom = sys.argv[1]
m1 = moment1(readFrom)
m2 = moment2(readFrom)
expMOM(m1)
ereMOM(m1, m2)
gammaMOM(m1, m2)
