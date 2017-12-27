import random
import os
import numpy as np
from collections import defaultdict


def main():
    
    startPrime = 4
    nextPrime = find_next_prime(startPrime)
    primeNumbers = [50]
    primeNumbers = fillArray()
    results = {}
    results = defaultdict(list)
    results.update({6:[()]})

    


                    #layout: oddnumer, summand1, summand2, summand3 -> 
                    #[oddnummber]   #[summands1[number][number][]number]    #[summands2][number][number]
    findSummands(primeNumbers, results)
    print "debug"
    print results
    print "debug2"
    print results.get(96)
   

def fillArray():
    c = 0
    primeNumbers = [100]
    primeNumbers[0] = 3
    prime = 3
    while c < 50:
        c+=1
        prime = find_next_prime(prime)
        primeNumbers.append(prime)

    return primeNumbers

def find_next_prime(n):
    return find_prime_in_range(n+1, 10000)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

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
                    print l
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


if __name__ == '__main__':
    main()