a = 1
b = 2
s = 0
c = 0
while c < 4000001:
    print(a)
    print(b)
    c = a + b
    if a%2 == 0:
        s = s + a
    if b%2 == 0:
        s = s + b
    a = c
    b = c + b
print("Answer: {}".format(s))