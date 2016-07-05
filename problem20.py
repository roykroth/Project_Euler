# I am doing this one in such a stupid way! But it works
def fact(n):
    if n == 2:
        return n
    else:
        return n*fact(n-1)

num = fact(100)
# Now just take the sum of the digits
l = list(str(num))
l = [int(i) for i in l]
print('Answer: {}'.format(sum(l)))
