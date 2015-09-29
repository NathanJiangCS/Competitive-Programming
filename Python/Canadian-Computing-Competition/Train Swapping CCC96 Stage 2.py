for zxc in xrange(int(raw_input())):
    n = int(raw_input())
    num = map(int,raw_input().split())
    c = 0
    sort = False
    while not sort:
        sort = True
        for i in xrange(n-1):
            if num[i] > num[i+1]:
                c += 1
                sort = False
                d = num[i+1]
                num[i+1] = num[i]
                num[i] = d
    print "Optimal train swapping takes %s swap(s)." % c
