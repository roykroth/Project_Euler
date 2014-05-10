# Problem 15
# (I got a little help from the internet on this one)

def pascals_triangle(n):
    n = n - 1
    a = [1, 1]
    for i in xrange(n):
        b = [1] + [a[i] + a[i + 1] for i in xrange(len(a) - 1)] + [1]
        a = b
    return b

print max(pascals_triangle(40))