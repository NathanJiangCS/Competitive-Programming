asd = int(raw_input())
for zxc in xrange(asd):
    x = 0; y = 0;
    di = 1;
    while 1:
        a = int(raw_input())
        if a == 0:
            break
        
        if a == 2:
            di += 1
            if di > 3:
                di = 0
        elif a == 3:
            di -= 1
            if di < 0:
                di = 3
        else:
            dist = int(raw_input())
            if di == 0:
                x -= dist
            elif di == 1:
                y += dist
            elif di == 2:
                x += dist
            elif di == 3:
                y -= dist

    print "Distance is %s" % (abs(x) + abs(y))
    if x == 0 and y ==0:

        pass
    else:
        if x > 0 and y > 0:
            if di == 2 or di == 3:
                while di != 3:
                    print 2
                    di += 1
                print 1
                print y
                print 2
                print 1
                print x
            else:
                while di != 0:
                    print 3
                    di -=1
                print 1
                print x
                print 3
                print 1
                print y

        elif x > 0 and y < 0:
            if di == 1 or di == 2:
                while di != 1:
                    di -= 1
                    print 3
                print 1
                print abs(y)
                print 3
                print 1
                print x
            elif di == 3:
                print 2
                print 1
                print x
                print 2
                print 1
                print abs(y)
            else:
                print 1
                print x
                print 2
                print 1
                print abs(y)
        elif x < 0 and y < 0:
            if di == 0 or di == 1:
                while di != 1:
                    di += 1
                    print 2
                print 1
                print abs(y)
                print 2
                print 1
                print abs(x)
            if di == 2 or di == 3:
                while di != 2:
                    di -= 1
                    print 3
                print 1
                print abs(x)
                print 3
                print 1
                print abs(y)
        elif x < 0 and y > 0:
            if di == 1 or di == 2:
                while di != 2:
                    di +=1
                    print 2
                print 1
                print abs(x)
                print 2
                print 1
                print y
            elif di == 0:
                print 3
                print 1
                print y
                print 3
                print 1
                print abs(x)
            else:
                print 1
                print y
                print 3
                print 1
                print abs(x)
        elif x == 0:
            if y > 0:
                if 1 <= di <= 3:
                    while di != 3:
                        di +=  1
                        print 2
                    print 1
                    print abs(y)
                else:
                    print 3
                    print 1
                    print abs(y)
            else:
                if 1 <= di <= 3:
                    while di != 1:
                        di -=1
                        print 3
                    print 1
                    print abs(y)
                else:
                    print 2
                    print 1
                    print abs(y)
        elif y == 0:
            if x > 0:
                if 0 <= di <= 2:
                    while di != 0:
                        di -= 1
                        print 3
                    print 1
                    print abs(x)
                else:
                    print 2
                    print 1
                    print abs(x)
            else:
                if 0 <= di <= 2:
                    while di != 2:
                        di += 1
                        print 2
                    print 1
                    print abs(x)
                else:
                    print 3
                    print 1
                    print abs(x)
    if zxc != asd-1:
        print
