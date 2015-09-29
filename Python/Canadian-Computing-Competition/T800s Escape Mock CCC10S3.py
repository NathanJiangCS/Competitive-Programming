r,c,k = map(int,raw_input().split())
grid = [[0 for i in xrange(c)] for j in xrange(r)]
dp = [[1e999 for i in xrange(c)] for j in xrange(r)]

for i in xrange(r):
    s = raw_input()
    for j in xrange(c):
        if s[j] == '.':
            grid[i][j] =1
        elif s[j] == 'R':
            grid[i][j] = 2

        elif s[j] == 'E':
            grid[i][j] =1
            goal = [i,j]
        elif s[j] == 'T':
            grid[i][j] =1
            start = [i,j]
q = [[start[0],start[1],k]]
dp[start[0]][start[1]] = 0
moves = [[1,0],[0,1],[-1,0],[0,-1]]
while len(q):
    a,b,e  = q.pop(0)
    for x,y in moves:
        x += a; y += b
        if 0 <= x < r and 0 <= y < c:
            if grid[x][y] != 0:
                if e != 0:
                    if dp[x][y] > dp[a][b] + 1:
                        dp[x][y] = dp[a][b] + 1
                        if grid[x][y] == 2:
                            d = k
                        else:
                            d = e - 1
                        q.append([x,y,d])
if dp[goal[0]][goal[1]] == 1e999:
    print 'T-800 Terminated.'
else:
    print dp[goal[0]][goal[1]]
