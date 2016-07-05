# Again, pretty inefficient, but I think it will be fast enough
def get_divisors(x):
    s = int(x**.5)
    divisors = [1]
    for i in range(2,s):
        oth = x/i
        if oth == int(oth):
            divisors.append(i)
            divisors.append(x//i)
    return sorted(set(divisors))

sumdiv = lambda x: sum(get_divisors(x))

def amicable(x):
    candidate = sumdiv(x)
    if sumdiv(candidate) == x and x != candidate:
        # Yay! Amicable
        return x, candidate
    else:
        return None

big = 10000
ami = []
for i in range(2,big):
    a = amicable(i)
    if a is not None:
        if a[1] < big:
            ami.append(i)
