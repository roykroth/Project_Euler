# Problem 3 from Project Euler
import sympy as sym
import numpy as np
from prime_seive import *
a = 600851475143 # Number we want to find largest prime factor of

def largest_prime_factor(X):
    top = X//2 
    succ = False
    i = 0
    while not succ:
        y = top - i
        if X % y == 0:
            succ = sym.primetest.isprime(y)
        i += 1
    return y

# print('Answer: {}'.format(largest_prime_factor(a)))

def lpf(X):
    '''
    Function to find the largest prime factor
    '''
    # Will end up duplicating some work, but what the heck.
    # First, make sure the number itself isn't prime
    top = int(X**2) # Will have a factor no larger than square root
    if is_prime(X):
        return X
    else:
        # It will be easiest to get the smaller factors first, I think...
        p = prime_gen() # Pops out prime numbers in order
        largest = 1
        for pr in p:
            if pr > top:
                break
            while X%pr == 0:
                X = X//pr # May as well make the problem smaller

    return largest

def rec_try(X):
    top = int(X**.5)
    if is_prime(X):
        return X
    else:
        p = prime_gen()
        # Find a prime divisor
        i = next(p)
        while X%i != 0:
            i = next(p)
        # Get through that when a prime divisor is found
        # The largest prime divisor of this number is the largest of the
        # original!
        return rec_try(X//i)



print("Answer: {}".format(rec_try(a)))





