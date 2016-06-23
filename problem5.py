# Problem 5

from prime_seive import *
def count_div(x, y):
    # How many times x goes into y
    i = 0
    while y%x == 0:
        y = y//x
        i += 1
    return i

def small(x):
    primes = primes_less_than(x+1)
    times = [1]*len(primes)
    for i in range(2,x+1):
        for j in range(len(times)):
            num = count_div(primes[j], i)
            if num > times[j]:
                times[j] = num
    # Now, we take the primes to the powers and multiply them
    final = 1
    for i, j in zip(primes, times):
        final *= i**j
    return final







def smallest_divis(x):
    # only trick is that if it is divisible by a number
    # divisible it is divisble. You need the minimum number
    nums = list(range(2, x+1))
    nums2 = nums
    for i in nums[::-1]:
        for j in nums:
            if i%j == 0 and i > j:
                nums.remove(j)
    prod = 1
    for i in nums:
        prod *= i
    return prod

print(smallest_divis(10))
