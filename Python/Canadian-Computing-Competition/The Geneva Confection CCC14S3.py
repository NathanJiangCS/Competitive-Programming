for zxc in xrange(int(raw_input())):
    a = int(raw_input())
    q = []
    b = []
    for i in xrange(a):
        q.append(int(raw_input()))
    c = 1
    y = True
    while len(q) or len(b):
        if len(q) and q[-1] == c:
            q.pop()
            c += 1
        elif len(b) and b[-1] == c:
            b.pop()
            c +=1
        else:
            b.append(q.pop())

        if not len(q):
            if len(b) and b[-1] != c:
                y = False
                break
    
    if y:
        print 'Y'
    else:
        print 'N'
