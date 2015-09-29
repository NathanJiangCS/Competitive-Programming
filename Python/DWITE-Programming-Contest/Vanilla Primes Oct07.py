a = input()

def prime(x):
    if x <= 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
    for i in range(3, int(x**.5)+1, 2):
        if x % i == 0:
            return False
    return True

if prime(a) :
    print "prime"

else:
    print"not"
