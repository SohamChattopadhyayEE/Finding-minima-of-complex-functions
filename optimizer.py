"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	

Coded by: Mukesh Saraswat (saraswatmukesh@gmail.com), Himanshu Mittal (emailid: himanshu.mittal224@gmail.com) and Raju Pal (emailid: raju3131.pal@gmail.com)
The code template used is similar given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.

 -- Purpose: Main File::
                Calling the Gravitational Search Algorithm(GSA) Algorithm 
                for minimizing of an Objective Function

Code compatible:
 -- Python: 2.* or 3.*
"""

import csv
import numpy
import time
import argparse

import OAs.GSA as gsa
import functions.benchmarks as benchmarks





def selector(algo,func_details,popSize,Iter):
    function_name=func_details[0]
    lb=func_details[1]
    ub=func_details[2]
    dim=func_details[3]
    

    if(algo==0):
        x=gsa.GSA(getattr(benchmarks, function_name),lb,ub,dim,popSize,Iter)    
    return x
    
    
# Select optimizers
GSA= True # Code by Himanshu Mittal



# Select benchmark function
F1=True # Sphere function
F2=True # Cigar or Bent Cigar function
F3=True # Rotated Hyper-ellipsoid (RHE) function
F4=True # Discus function
F5=True # Zettl function
F6=True # Leon function
F7=True # Easom function
F8=True # Schwefel 1.2 function
F9=True # Schwefel 2.2 function
F10=True # Rastrigin function
F11=True # Schwefel 2.26 function
F12=True # Styblinski-Tang (ST) function
F13=True # Schaffer F2 function
F14=True # Schaffer F6 function
F15=True # Bird function
F16=True # Rosenbrock function
F17=True # Griewank function 
F18=True # Trigonometric function 
F19=True # Hybrid function – 3 
F20=True # Hybrid function – 1  

Algorithm=[GSA]
objectivefunc=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19] 
        
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
Runs=1

# Select general parameters for all optimizers (population size, number of iterations)
PopSize = 50
iterations= 200

#Export results ?
Export=True


#ExportToFile="YourResultsAreHere.csv"
#Automaticly generated name by date and time
ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 

# Check if it works at least once
atLeastOneIteration=False


# CSV Header for for the cinvergence 
CnvgHeader=[]

for l in range(0,iterations):
	CnvgHeader.append("Iter"+str(l+1))


for i in range (0, len(Algorithm)):
    for j in range (0, len(objectivefunc)):
        if((Algorithm[i]==True) and (objectivefunc[j]==True)): # start experiment if an Algorithm and an objective function is selected
            for k in range (0,Runs):
                
                func_details=benchmarks.getFunctionDetails(j)
                x=selector(i,func_details,PopSize,iterations)
                if(Export==True):
                    with open(ExportToFile, 'a') as out:
                        writer = csv.writer(out,delimiter=',')
                        if (atLeastOneIteration==False): # just one time to write the header of the CSV file
                            header= numpy.concatenate([["Optimizer","objfname","startTime","EndTime","ExecutionTime"],CnvgHeader])
                            writer.writerow(header)
                        a=numpy.concatenate([[x.Algorithm,x.objectivefunc,x.startTime,x.endTime,x.executionTime],x.convergence])
                        writer.writerow(a)
                    out.close()
                atLeastOneIteration=True # at least one experiment
                
if (atLeastOneIteration==False): # Faild to run at least one experiment
    print("No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions") 
        
        