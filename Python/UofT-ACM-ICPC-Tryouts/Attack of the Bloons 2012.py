for zxc in xrange(int(raw_input())):
    l,n = map(int,raw_input().split())
    grid = [0 for i in xrange(l+10)]
    for i in xrange(n):
        c,r,d = map(int,raw_input().split())
        start = c-r; end = c+r;
        if start <= 0:
            start = 1
        if end > l:
            end = l
        grid[start] += d; grid[end+1] -= d;
    m = int(raw_input())
    for i in xrange(1,l+1):
        grid[i] += grid[i-1]
    for i in xrange(m):
        a = int(raw_input())
        leak = True
        for j in xrange(1,l+1):
            a -= grid[j]
            if a <= 0:
                print j
                leak = False
                break
        if leak:
            print 'Bloon leakage'
            
