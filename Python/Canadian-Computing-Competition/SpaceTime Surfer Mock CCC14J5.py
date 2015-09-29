#import sys
#sys.stdin = open('yes.txt','r')

r,c,t = map(int,raw_input().split())

adj = [[[False for i in xrange(c)] for j in xrange(r)] for k in xrange(t)]
flag = [[[False for i in xrange(c)] for j in xrange(r)] for k in xrange(t)]
dp = [[[99999 for i in xrange(c)] for j in xrange(r)] for k in xrange(t)]

for zxc in range(t):
    for j in range(r):
        a = raw_input()
        for i in range(len(a)):
            if a[i] == '.':
                adj[zxc][j][i] = True
            elif a[i] == 'A':
                sx = i
                sy = j
                sz = zxc
                adj[zxc][j][i] = True
            elif a[i] == 'B':
                fx = i
                fy = j
                fz = zxc
                adj[zxc][j][i] = True

flag[sz][sy][sx] = True
dp[sz][sy][sx] = 0
q = [[sz,sy,sx]]
goto = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1]]


while len(q) > 0:
    z,y,x = q.pop(0)
    for i in goto:
        gox,goy,goz = i
        if gox == 0 and goy == 0 and goz == 1:        
            for j in range(t):
                if j != z:
                    goz = j
                    if adj[goz][y][x]:
                        if not flag[goz][y][x]:
                            flag[goz][y][x] = True
                            dp[goz][y][x] = (dp[z][y][x] + 1)
                            q.append([goz,y,x])
                            
        else:
            gox += x
            goy += y
            if gox < 0 or gox >(c-1) or goy < 0 or goy>(r-1):
                pass
            else:
                if adj[z][goy][gox]:
                    if not flag[z][goy][gox]:
                        flag[z][goy][gox] = True
                        dp[z][goy][gox] = (dp[z][y][x] + 1)
                        q.append([z,goy,gox])
if dp[fz][fy][fx] == 99999:
    print -1
else:
    print dp[fz][fy][fx]
