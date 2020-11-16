# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:37:38 2020
calc prime number
@author: Rick
"""

primes= []
primes.append(2)
primes.append(3)

def IsPrime(n):
    if(n>(primes[-1]*2)):
        return -1
    for num in primes:
        if n%num==0 and n!=num:
            return False
    return True

#print(IsPrime(7))

for i in range(2,1000):
    if IsPrime(i) and i>primes[-1]:
        primes.append(i)
        
print(primes)
