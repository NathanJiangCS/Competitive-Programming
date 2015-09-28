#import sys
#sys.stdin = open('test.txt', 'r')
a = input()
adj = [[] for i in xrange(9999)]

for i in xrange(a):
    b,c = map(int, raw_input().split())
    b -= 1
    c -= 1
    adj[b].append(c)

b,c = 1,1
while b != 0 or c != 0:
    b,c = map(int, raw_input().split())
    if b != 0 or c != 0:
        connect = False
        dos = 0
        b -= 1
        c -= 1
        q = [b]
        flag = [False for i in xrange(9999)]
        dp = [99999 for i in xrange(9999)]
        dp[b] = 0
        flag[b] = True
        while len(q):
            u = q.pop(0)
            for i in adj[u]:
                if i == c:
                    connect = True
                    dos = dp[u]
                    break
                else:
                    if flag[i] == False:
                        flag[i] = True
                        q.append(i)
                        dp[i] = (dp[u] + 1)
        if connect:
            print 'Yes %s' % dos
        else:
            print 'No'
