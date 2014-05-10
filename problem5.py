# Problem 5
from prime_seive import is_prime
count = 0
num = 0
while count < 10001:
    num += 1
    if is_prime(num):
        count += 1

print num