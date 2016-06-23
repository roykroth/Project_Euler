# Problem 15

# Pretty simple conceptually. You need 20 rights and 20 downs, can put them
# in any order. I just need to figure out how to count them all.

def fact(x):
    # Simple factorial
    if x < 1:
        raise Exception
    elif x == 2:
        return 2
    else:
        return x*fact(x-1)

num = fact(40)/(fact(20)**2)
