# Problem 12
def trianges():
    i = 1
    num = 1
    while True:
        yield num
        i += 1
        num += i

def count_divisors(n):
    divs = 2 # 1 divides everything
    if n > 2:
        for i in range(2, int(n**.5)):
            if n % i == 0:
                divs += 2
    return divs

done = False
a = trianges()
while not done:
    num = next(a)
    if count_divisors(num) > 500:
        done = True

print(num)
