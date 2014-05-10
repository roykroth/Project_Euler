# Problem 11
import numpy as np
a = np.loadtxt('nums_for_11.txt')

# Find Max Column product
col_max = 0
for i in xrange(16):
    b = a[i:i+4,:].prod(axis = 0)
    c = b.max()
    if c > col_max:
        col_max = c
print 'Max Column Prod: %i' %col_max

# Find Max Row product
row_max = 0
for i in xrange(16):
    b = a[:,i:i+4].prod(axis = 1)
    c = b.max()
    if c > row_max:
        row_max = c
print 'Max Column Prod: %i' %row_max


# Now, Find the max diagonal. This one will be harder... but with clever use
# of diagonals it is not too bad
down_col = 0
for i in xrange(-16, 17):
    diag = np.diag(a, i)
    for j in xrange(17 - abs(i)):
        num = diag[j:j+4].prod()
        if num > down_col:
            down_col = num

print 'Max Down Col: %i' %down_col

up_col = 0
for i in xrange(-16, 17):
    diag = np.diag(a[:, ::-1], i)
    for j in xrange(17 - abs(i)):
        num = diag[j:j+4].prod()
        if num > up_col:
            up_col = num

print 'Max up Col: %i' %up_col



print 'Max: %i' %max([up_col, down_col, row_max, col_max])