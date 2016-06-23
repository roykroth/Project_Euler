import itertools as it
def is_prime(n):
    if n < 2:
        return False
    limit = int(n**0.5)
    sieve = [True] * (limit + 1)   
    for i in range(2, limit + 1):
        if sieve[i]:
            if n % i == 0:
                return False # If divisible not prime
            else:
                sieve[i::i] = [False]*len(sieve[i::i]) # If not divisible
                # will not be divisible by anyrhing divisible by it. 
    return True

def primes_less_than(n):
    size = int(n)//2 # At most 2 and odds will be prime
    sieve = [True]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        # If prime
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [False]*tmp
    return [2] + [i*2 + 1 for i, v in enumerate(sieve) if v and i >= 1]

def prime_gen():
    # Not my work. Got from erat3 on 
    #https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )
    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p

