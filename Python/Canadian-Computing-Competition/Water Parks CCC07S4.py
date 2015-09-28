def paths(x):
    if x == n:
        return 1
    else:
        c = 0
        for v in adj[x]:
            if path[v] == -1:
                path[v] = paths(v)
            c += path[v]
        return c
n = int(raw_input())
adj = [[] for i in xrange(n+2)]
path = [-1 for i in xrange(n+2)]
while 1:
    a,b = map(int,raw_input().split())
    if a == 0 and b == 0:
        break
    else:
        adj[a].append(b)
print paths(1)
