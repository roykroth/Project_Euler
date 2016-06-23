# Problem 17
def to_word_basic(x):
    assert x == int(x)
    wa = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    wb = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wc = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if x == 0:
        return ''
    if x < 10:
        return wa[x-1]
    elif 10 <= x < 20:
        return wb[x-10]
    elif x in [10*i for i in range(2, 10)]:
        x = x//10
        return wc[x-2]
    else:
        raise NotImplementedError

def to_word(x):
    word = ''
    thousands = x // 1000
    hundreds = (x%1000) // 100
    x = x%100
    # Do the thousands and hundreds
    if thousands > 0:
        word += to_word_basic(thousands) + ' thousand'
    if hundreds > 0:
        word += ' ' + to_word_basic(hundreds) + ' hundred'
        if x > 0:
            word += ' and'
    if x < 20:
        word += ' ' + to_word_basic(x)
    else:
        tens = x // 10
        x = x % 10
        word += ' ' + to_word_basic(10*tens) + ' ' + to_word_basic(x)
    word = ' '.join(word.split())
    return word

words = [to_word(i) for i in range(1, 1001)]
words_nospace = [''.join(i.split()) for i in words]
mashup = ''.join(words_nospace)
letters = len(mashup)
print('Number of Letters: {}'.format(letters))
