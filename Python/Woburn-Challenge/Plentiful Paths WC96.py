c,d = map(int,raw_input().split())
dp = [[-1e999 for i in xrange(d)] for j in xrange(c)]
aps = [[0 for i in xrange(d)] for j in xrange(c)]

a = 1; b = 1
while a != 0 or b!=0:
    a,b = map(int,raw_input().split())
    if a != 0 and b != 0:
        aps[a-1][b-1] = 1
        
if aps[0][0] == 1:
    dp[0][0] = 1
else:
    dp[0][0] = 0
moves = [[0,1],[1,0]]
q = [[0,0]]
while len(q):
    x,y= q.pop(0)
    for i in moves:
        x1 ,y1 = i
        x1 += x; y1 += y
        if 0 <= x1 < d and 0 <= y1 < c:
            if dp[y][x] + aps[y1][x1] > dp[y1][x1]:
                dp[y1][x1] = dp[y][x] + aps[y1][x1]
                q.append([x1,y1])

print dp[c-1][d-1]
