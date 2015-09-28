#import sys
#sys.stdin = open('test.txt','r')
def move(x,y,m):#m=0 is right, m=1 is up, m=2 is down
    if x < 1 or x > r or y < 1 or y > c:
        return -1e999
    else:
        if grid[x][y] != -1:
            if x == r and y == c:
                return grid[r][c]
            else:
                if m == 0:#go up, down, right
                    if memo[x][y+1][0] == -1:
                        memo[x][y+1][0] = move(x,y+1,0)
                    if memo[x+1][y][1] == -1:
                        memo[x+1][y][1] = move(x+1,y,1)
                    if memo[x-1][y][2] == -1:
                        memo[x-1][y][2] = move(x-1,y,2)
                    return max(memo[x][y+1][0]+grid[x][y], memo[x+1][y][1]+grid[x][y], memo[x-1][y][2]+grid[x][y])
                elif m == 1:
                    if memo[x][y+1][0] == -1:
                        memo[x][y+1][0] = move(x,y+1,0)
                    if memo[x+1][y][1] == -1:
                        memo[x+1][y][1] = move(x+1,y,1)
                    return max(memo[x][y+1][0]+grid[x][y], memo[x+1][y][1]+grid[x][y])
                elif m == 2:
                    if memo[x][y+1][0] == -1:
                        memo[x][y+1][0] = move(x,y+1,0)
                    if memo[x-1][y][2] == -1:
                        memo[x-1][y][2] = move(x-1,y,2)
                    return max(memo[x][y+1][0]+grid[x][y], memo[x-1][y][2]+grid[x][y])
        else:
            return -1e999
while 1:
    r,c = map(int,raw_input().split())
    if r ==0 and c == 0:
        quit()
    grid = [[0 for j in xrange(c+1)] for i in xrange(r+1)]
    memo = [[[-1 for i in xrange(3)] for j in xrange(c+5)] for k in xrange(r+5)]
    for i in xrange(r):
        a = raw_input()
        for j in xrange(c):
            if a[j] == '*':
                grid[i+1][j+1] = -1
            elif a[j] != '.':
                p = int(a[j])
                grid[i+1][j+1] = p
    print move(r,1,0)
