n,w,p = map(int,raw_input().split())
d = [[] for i in xrange(n)]
for i in xrange(w):
    a,b,c = map(int,raw_input().split())
    a -= 1; b -=1
    d[a].append([b,c])
    d[b].append([a,c])
for zxc in xrange(p):
    dp = [1e999 for i in xrange(n)]
    start, end = map(int,raw_input().split())
    start -= 1; end -= 1;
    dp[start] = 0
    q = [start]
    while len(q):
        u = q.pop(0)
        for x,y in d[u]:
            if dp[u] + y < dp[x]:
                dp[x] = dp[u] + y
                q.append(x)
    print dp[end]
