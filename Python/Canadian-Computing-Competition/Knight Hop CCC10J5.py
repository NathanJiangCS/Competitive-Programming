sx, sy = map(int,raw_input().split())
fx,fy = map(int,raw_input().split())
sx = sx - 1
sy = sy - 1
fx = fx - 1
fy = fy - 1
possiblemoves = [[1,2],[2,1],[2,-1],[1,-2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

dp = [[99999 for i in xrange(8)] for j in xrange(8)]
flag = [[False for i in xrange(8)] for j in xrange(8)]
dp[sx][sy] = 0
flag[sx][sy] = True
q = [[sx,sy]]

while len(q) > 0:
    x,y = q.pop(0)
    for i in possiblemoves:
        gox,goy = i
        gox += x
        goy += y
        if gox < 0 or gox > 7 or goy < 0 or goy > 7:
            pass
        else:
            if flag[gox][goy] == False:
                flag[gox][goy] = True
                dp[gox][goy] = (dp[x][y] + 1)
                q.append([gox,goy])

print dp[fx][fy]
