from prime_seive import is_prime

want_prime = 10001
num_primes = 0
i = 1

while True:
    if is_prime(i):
        num_primes += 1
        if num_primes == want_prime:
            break
    i += 1

print i
