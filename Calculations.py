#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:06:32 2017

@author: makishimizu
"""

import numpy
from numpy.linalg import inv

#histogram data h, (N, 3) matrix 
#ROUNDING
h = numpy.array([[1.0,2.0,3.0],[3.0,4.0,5.0],[7.0,8.0,9.0],[2.0,5.0,7.0]])

def alpha(h):
    rSum = 0 # running sum 
    for i in range (len(h)):
        sig = h[i][2] #Nth row 3rd position in matrix, i.e. sigma_n
        rSum = rSum + 1/sig**2 
    return rSum

def beta(h):
    rSum = 0
    for i in range (len(h)):
        x = h[i][0] #Nth row 1st position in matrix, i.e. x_n
        sig = h[i][2]
        rSum = rSum + x/sig**2
    return rSum

def gamma(h):
    rSum = 0 
    for i in range (len(h)):
        y = h[i][1] #Nth row 2nd position in matrix, i.e. y_n
        sig = h[i][2]
        rSum = rSum + y/sig**2
    return rSum
        
def lam(h):
    rSum = 0 
    for i in range (len(h)):
        x = h[i][0] 
        sig = h[i][2]
        rSum = rSum + (x**2)/(sig**2)
    return rSum
        
        
def rho(h):
    rSum = 0 
    for i in range (len(h)):
        x = h[i][0] 
        y = h[i][1]
        sig = h[i][2]
        rSum = rSum + (x*y)/sig**2
    return rSum
    
    
uninvM =  numpy.matrix([[alpha(h), beta(h)],[beta(h),lam(h)]])
invM = inv(uninvM)

def a(invM):
        total = invM[0,0]*gamma(h) + invM[0,1]*rho(h)
        return total

def aVar(invM):
    return invM[0,0]

def b(invM):
    total = invM[1,0]*gamma(h) + invM[1,1]*rho(h)
    return total
    
    
def bVar(invM):
    return invM[1,1]
       
print a(invM)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
