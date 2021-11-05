# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	

Coded by: Mukesh Saraswat (saraswatmukesh@gmail.com), Himanshu Mittal (emailid: himanshu.mittal224@gmail.com) and Raju Pal (emailid: raju3131.pal@gmail.com)
The code template used is similar given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.

 -- Purpose: Defining the benchmark function code 
              and its parameters: function Name, lowerbound, upperbound, dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math


    
def F1(x):
  """ Spere Function """
  s=numpy.sum(x**2)
  return s

def F2(x):
  """Cigar or Bent Cigar function"""
  s = x[0]**2 + (10**6) * numpy.sum(x[1 :]**2)
  return s

def F3(x):
  """Rotated Hyper-ellipsoid (RHE) function"""
  s = numpy.sum(numpy.sum(x**2))
  return s

def F4(x):
  """Discus function"""
  s = (10**6) * (x[0]**2) + numpy.sum(x[1 :]**2)
  return s

def F5(x):
  """Zettl function"""
  s = (1/4)*x[0] + (x[0]**2 - 2*x[0] + x[1]**2)**2
  return s

def F6(x):
  """Leon function"""
  s = 100*(x[1]-x[0]**2)**2+(1-x[0])**2
  return s

def F7(x):
  """Easom function"""
  s = -math.cos(x[0])*math.cos(x[1])*math.exp(-(x[0] - math.pi)**2 - (x[1]-math.pi)**2)
  return s

def F8(x):
  """Schwefel 1.2 function"""
  s = numpy.sum((numpy.sum(x))**2)
  return s

def F9(x):
  """Schwefel 2.2 function"""
  s = numpy.sum(abs(x))+numpy.prod(abs(x))
  return s

def F10(x):
  """Rastrigin function"""
  sum = 0
  for i in range(len(x)):
    sum += x[i]**2 - 10*math.cos(2*math.pi*x[i])
  s = 10*len(x) + sum
  return s

def F11(x):
  """Schwefel 2.26 function"""
  sum = 0
  for i in range(len(x)):
    sum += x[i] * math.sin(math.sqrt(abs(x[i])))
  s = 418.9829*len(x) + sum
  return s

def F12(x):
  """Styblinski-Tang (ST) function"""
  s = (1/2)*numpy.sum(x**4 - 16*(x**2)+5*x)
  return s

def F13(x):
  """Schaffer F2 function"""
  s = 0.5 + ((math.sin(x[0]**2-x[1]**2))**2-0.5)/(1+0.001*(x[0]**2+x[1]**2))
  return s

def F14(x):
  """Schaffer F6 function"""
  s = 0.5 + ((math.sin(math.sqrt(x[0]**2+x[1]**2)))**2-0.5)/(1+0.001*(x[0]**2+x[1]**2))
  return s

def F15(x):
  """Bird function """
  s = (x[0]-x[1])**2+math.cos(x[1])*math.exp((1-math.sin(x[0]))**2)
  return s
'''
def F16(x):
  """Ackley function"""
  a = 20
  b = 0.2
  c = 2*math.pi
  d = len(x)
  s = -a*math.exp(-b*math.sqrt((1/d)*numpy.sum(x**2)))-math.exp((1/d)*numpy.sum(math.cos(c*x)))+a+math.e
  return s
'''
def F16(x):
  """Rosenbrock function"""
  sum = 0
  for i in range(len(x)-1):
    sum += 100*(x[i+1]-x[i]**2)**2+(x[i]+1)**2
  return sum

def F17(x):
  """Griewank function """
  sum = 0
  prod = 1
  for i in range(len(x)):
    sum += x[i]/4000
    prod *= math.cos(x[i]/math.sqrt(i+1))
  s = sum - prod + 1
  return s

def F18(x):
  """Trigonometric function """
  s = 0
  m = 0
  for i in range(len(x)):
    m += math.cos(x[i])
  for i in range(len(x)):
    s += (i+1)*(1-math.cos(x[i]))-math.sin(x[i])-m
  return s

def F19(x):
  """Hybrid function – 3"""
  s = F17(x)+F16(x)+F4(x)
  return s

def F20(x):
  """Hybrid function – 1"""
  s = F10(x)+F2(x)+F17(x)
  return s

def getFunctionDetails(a):
  # [name, lb, ub, dim]
  param = {  0: ["F1",-100,100,30],
             1: ["F2",-100,100,30],
             2: ["F3",-100,100,30],
             3: ["F4",-100,100,30],
             4: ["F5",-5,5,30],
             5: ["F6",-1.2,1.2,30],
             6: ["F7",-100,100,30],
             7: ["F8",-100,100,30],
             8: ["F9",-100,100,30],
             9: ["F10",-5.2,5.2,30],
             10: ["F11",-500,500,30],
             11: ["F12",-5,5,30],
             12: ["F13",-100,100,30],
             13: ["F14",-100,100,30],
             14: ["F15",-1.582142,-3.130247,30],
             15: ["F16",-30,30,30],
             16: ["F17",-600,600,30],
             17: ["F18",-1000,1000,30],
             18: ["F19",-100,100,30],
             18: ["F20",-100,100,30],
            }

  return param.get(a, "nothing")



