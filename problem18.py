# with open('nums_for_18.tex') as f:
with open('p067_triangle.txt') as f:
    numbers = f.readlines()
for i in range(len(numbers)):
    numbers[i] = numbers[i].split()
    numbers[i] = [int(j) for j in numbers[i]]

# Now that I have everything in a nice package I can do the maximization
for i in range(len(numbers)-1):
    for j in range(len(numbers[i+1])):
        if j==0:
            numbers[i+1][0] = numbers[i+1][0] + numbers[i][0]
        elif j == len(numbers[i]):
            numbers[i+1][j] = numbers[i+1][j] + numbers[i][j-1]
        else:
            numbers[i+1][j] = numbers[i+1][j] + max(numbers[i][j-1],numbers[i][j])
last = numbers[-1]
themax = max(last)
print('Maximum Path Sum: {}'.format(themax))
