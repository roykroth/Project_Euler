# Problem 9 Solution
# This isn't that elegant, but it works
from itertools import product
for a, b in product(xrange(500), xrange(500)):
    c = (a**2 + b**2)**.5
    if c == int(c):
        if a + b + c == 1000:
            print a*b*c
            break

print a, b, c