# Problem 3 from Project Euler
from prime_seive import prime_seive
import sympy as sym
import numpy as np
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