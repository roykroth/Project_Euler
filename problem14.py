import numpy as np

def collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        yield n

def coll_len(n):
    return len([i for i in collatz(n)])

longest = 0
longest_num = 3

for i in xrange(3, int(1e6)):
    l = coll_len(i)
    if l > longest:
        longest = l
        longest_num = i

print longest_num