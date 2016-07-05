with open('p022_names.txt') as f:
    names = f.readlines()[0]
names = names.split(',')
names = sorted(names)
def scoreletter(let):
    # Score a letter
    letdict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P':16, 'Q': 17,
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    try:
        score = letdict[let]
    except:
        score = 0
    return score

def score(name):
    # Name is a string
    name = name.upper()
    l = list(name)
    nums = [scoreletter(i) for i in l]
    return sum(nums)

namescores = [score(i) for i in names]
total = 0
for i, j in enumerate(namescores):
    total += (i+1)*j

print('Total: {}'.format(total))
