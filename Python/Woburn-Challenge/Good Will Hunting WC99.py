a = 1
while a != 0:
    a = input()
    if (0 < a < 1):
        c = 0
        while a < 1:
            a = a * 10
            c = c + 1
        print "%.3f x 10^-%s" %(a, c)
    elif (1 <= a < 10) or (-10 < a <= -1):
        print "%.3f" % (a)
    elif (-1 < a < 0):
        c = 0
        while a > -1:
            a = a * 10
            c = c + 1
        print "%.3f x 10^-%s" %(a, c)
    elif (10 <= a):
        c = 0
        while a >= 10:
            a = a / 10
            c = c + 1
        print "%.3f x 10^%s" % (a, c)
    
    elif (a <= -10):
        c = 0
        while a <= -10:
            a = a / 10
            c = c + 1
        print "%.3f x 10^%s" % (a, c)
