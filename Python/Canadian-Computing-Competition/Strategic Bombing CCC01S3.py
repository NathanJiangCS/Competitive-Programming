dp = [99999 for i in xrange(26)]
adj = [[False for i in xrange(26)] for j in xrange(26)]
flag = [False for i in xrange(26)]
a = 1
dp[0] = 0
roads = []
rtb = []
while a != '**':
    a = raw_input()
    roads.append(a)
    if a != '**':
        loca = (ord(a[0]) - 65)
        locb = (ord(a[1]) - 65)
        adj[loca][locb] = True
        adj[locb][loca] = True

for i in roads:
    q = [0]
    loca = (ord(i[0]) - 65)
    locb = (ord(i[1]) - 65)
    adj[loca][locb] = False
    adj[locb][loca] = False
    while len(q) > 0:
        u = q.pop(0)
        for j in range(26):
            if adj[u][j]:
                if not flag[j]:
                    flag[j] = True
                    q.append(j)
                    dp[j] = (dp[u]+1)
    if dp[1] == 99999:
        rtb.append(i)
        
    dp = [99999 for i in xrange(26)]
    flag = [False for i in xrange(26)]
    adj[loca][locb] = True
    adj[locb][loca] = True
    dp[0] = 0

for i in rtb:
    print i
print 'There are %s disconnecting roads.' % len(rtb)
