# I am going to do this the most naive way possible

a = 2**1000
b = str(a)
s = 0
for i in b:
    s += int(i)

print s
