def is_palindrome(x):
    pal = False
    if x == int(str(x)[::-1]):
        pal = True
    return pal

largest = -1
from itertools import product
for x, y in product(range(100, 1000), range(100, 1000)):
    prod = x*y
    if is_palindrome(prod) and prod > largest:
        largest = prod

print(largest)