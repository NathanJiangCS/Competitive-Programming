for zxc in xrange(int(raw_input())):
    u = int(raw_input()); o = 0; e = 0
    c = 0
    print 'Round 0: %s undefeated, 0 one-loss, 0 eliminated' % u
    while u + o > 1:
        c += 1
        if u == 1 and o == 1:
            u -= 1; o += 1
            print 'Round %s: %s undefeated, %s one-loss, %s eliminated' % (c,u,o,e)
            c += 1; o -= 1; e += 1
            print 'Round %s: %s undefeated, %s one-loss, %s eliminated' % (c,u,o,e)
            print 'There are %s rounds.' % c
            break
        else:
            if o > 1:
                x = o - o/2
                e += (o-x)
                o = x
            if u > 1:
                x = u - u/2
                o += (u-x)
                u = x
        print 'Round %s: %s undefeated, %s one-loss, %s eliminated' % (c,u,o,e)
