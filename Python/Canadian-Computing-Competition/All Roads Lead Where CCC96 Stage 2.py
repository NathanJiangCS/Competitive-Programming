m,n = map(int,raw_input().split())
dic = {'Rome': 0}
c = 1
paths = []
for i in xrange(m):
    a,b = raw_input().split()
    if a not in dic:
        dic[a] = c
        c += 1
    if b not in dic:
        dic[b] = c
        c += 1
    paths.append((a,b))
grid = [[] for i in xrange(len(dic))]
for x,y in paths:
    x = dic[x]; y = dic[y]
    grid[x].append(y)
    grid[y].append(x)
keys = sorted(dic, key=dic.get)
for zxc in xrange(n):
    a,b = raw_input().split()
    a = dic[a]; b = dic[b]
    parentnode = [-1 for i in xrange(len(dic))]
    dp = [1e999 for i in xrange(len(dic))]
    flag = [False for i in xrange(len(dic))]
    q = [a]
    dp[a] = 0
    flag[a] = True
    while len(q):
        u = q.pop(0)
        for i in grid[u]:
            if not flag[i]:
                dp[i] = dp[u] + 1
                flag[i] = True
                q.append(i)
                parentnode[i] = u

    s = ''
    s += keys[b][0]
    while b != -1:
        b = parentnode[b]
        if b != -1:
            s += keys[b][0]
    print s[::-1]
