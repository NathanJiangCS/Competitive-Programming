def upc(x):
    x = list(x)
    even = 0
    odd = 0
    for i in xrange(len(x)):
        j = i + 1
        if j % 2 == 0:
            even += int(x[i])
        else:
            odd += int(x[i])
    if (even + 3 * odd) % 10 == 0:
        return True
    else:
        return False
    
for zxc in xrange(5):
    a = raw_input()
    l = []
    for i in xrange(12):
        for j in xrange(10):
            k = a[:i] + str(j) + a[i+1:]
            if upc(k):
                l.append(k)
                break
    print l[-1]      
