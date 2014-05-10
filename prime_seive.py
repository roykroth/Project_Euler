def is_prime(n):
    if n < 2:
        return False
    limit = int(n**0.5)
    sieve = [True] * (limit + 1)   
    length = len(sieve)
    for i in range(limit + 1):
        if i > 1 and sieve[i]:
            if n % i == 0:
                return False
            else:
                sieve[i::i] = [False]*len(sieve[i::i])
    return True

def primes_less_than(n):
    size = int(n)//2
    sieve = [True]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [False]*tmp
    return [2] + [i*2 + 1 for i, v in enumerate(sieve) if v and i >= 1]
