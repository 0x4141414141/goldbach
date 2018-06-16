import random
import os
import numpy as np
from collections import defaultdict
from primesieve import *
from primesieve.numpy import *
import random
import sys
import array
import matplotlib.pyplot as plt
#python2.7
#install numpy

def main():

    #generate Primenumbers with primesieve and save in list
    primeNumbers = n_primes(200)
    print primeNumbers[199]

    results = {}

    results = defaultdict(list)

    results.update({6:[()]})
    #layout: oddnumer, summand1, summand2, summand3 -> 

    #[evennumber]   #[summands1[prime1][prime2][]prime3]    #[summands2][....]]

    findSummands(primeNumbers, results)
    #print results

    print "debug2"

    print results.get(521)
    plot()


   
def findSummands(primeNumbers, results):
    findValue = 6
    summand1 = 0
    summand2 = 0
    while findValue < 1000:
        i=0
        while i<len(primeNumbers)-1:
            c=0
            #iterate over first summand
            summand1 = primeNumbers[i]
            while c<len(primeNumbers)-1:
            #iterate over second summand
                summand2 = primeNumbers[c]
                #print summand2
                #print summand1
                if summand1 + summand2 == findValue:
                    #declare list and append to dict
                    summands = [summand1,summand2]
                    l = results.get(6)
                    #print l
                    results[findValue].append(summands)
                    #results.update({findValue:[summands]})
                    #z is the even number; i is the number(count) of entry ; c[0] is first summand, c[1] second summand    
                c+=1
            i+=1
        findValue = findValue+2
    return results
	

def saveResults(results, primenumber, factor):
#layout: [primenumber][factor1,factor2,factor3] ; append size?
	#search for prime / maybe remember last prime -> faster
	#append found factors
	return 1

def plot():
    test = {1092268: [81, 90], 524292: [80, 80], 892456: [88, 88]}


    data = {"x":[], "y":[], "label":[]}
    for label, coord in test.items():
        data["x"].append(coord[0])
        data["y"].append(coord[1])
        data["label"].append(label)

    # display scatter plot data
    plt.figure(figsize=(10,8))
    plt.title('Scatter Plot', fontsize=20)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.scatter(data["x"], data["y"], marker = 'o')
    
    # add labels
    for label, x, y in zip(data["label"], data["x"], data["y"]):
        plt.annotate(label, xy = (x, y))


if __name__ == '__main__':
    main()