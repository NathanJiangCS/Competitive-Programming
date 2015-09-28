def monkey(x):
    if aword(x):
        return True
    elif 'N' in x:
        for i in xrange(1, len(x)-1):
            if x[i] == 'N':
                if aword(x[0:i]) and monkey(x[i+1:]):
                    return True
        return False
    else:
        return False
def aword(x):
    if x == 'A':
        return True
    elif len(x)>2:
        if x[0] == 'B' and x[-1] == 'S':
            if monkey(x[1:-1]):
                return True
            else:
                return False
    else:
        return False
while 1:
    a = raw_input()
    if a == 'X':
        quit()
    else:
        if monkey(a):
            print 'YES'
        else:
            print 'NO'
