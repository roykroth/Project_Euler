a = 1
b = 1
sum = 0
c = 0
while c < 4000001:
    c = a + b
    sum = sum + c
    a = c + b
    b = c + a
print sum