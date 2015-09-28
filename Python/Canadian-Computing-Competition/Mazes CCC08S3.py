moves = [[0,1],[0,-1],[1,0],[-1,0]]
moves1 = [[1,0],[-1,0]]
moves2 = [[0,1],[0,-1]]

for zxc in xrange(int(raw_input())):
    r = int(raw_input()); c = int(raw_input())
    grid = []
    flag = [[False for i in xrange(c)] for j in xrange(r)]
    dp = [[1e999 for i in xrange(c)] for j in xrange(r)]
    for i in xrange(r):
        grid.append(list(raw_input()))
    q = [[0,0]]
    dp[0][0] = 1
    flag[0][0] = True

    while len(q):
        a,b = q.pop(0)
        if grid[a][b] == '+':
            for x,y in moves:
                x += a; y += b
                if 0 <= x < r and 0 <= y < c and grid[x][y] != '*':
                    if not flag[x][y]:
                        flag[x][y] = True
                        dp[x][y] = dp[a][b] + 1
                        q.append([x,y])

        elif grid[a][b] == '-':
            for x,y in moves2:
                x += a; y += b
                if 0 <= x < r and 0 <= y < c and grid[x][y] != '*':
                    if not flag[x][y]:
                        flag[x][y] = True
                        dp[x][y] = dp[a][b] + 1
                        q.append([x,y])
        elif grid[a][b] == '|':
            for x,y in moves1:
                x += a; y += b
                if 0 <= x < r and 0 <= y < c and grid[x][y] != '*':
                    if not flag[x][y]:
                        flag[x][y] = True
                        dp[x][y] = dp[a][b] + 1
                        q.append([x,y])
    if dp[r-1][c-1] == 1e999:
        print -1
    else:
        print dp[r-1][c-1]
