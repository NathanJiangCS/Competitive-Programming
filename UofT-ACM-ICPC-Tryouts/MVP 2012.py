g = int(raw_input())
moves = [(1,0),(0,1), (-1, 0), (0,-1)]
for zxc in xrange(g):
    h,w = map(int,raw_input().split())
    graph = []; minerals = []
    flag = [[False for i in xrange(w)] for j in xrange(h)]
    dp = [[1e999 for i in xrange(w)] for j in xrange(h)]
    for i in xrange(h):
        a = raw_input()
        graph.append(a)
        for j in xrange(w):
            if a[j] == 'P':
                probe = (i,j)
            elif a[j] == 'C':
                cannon = (i,j)
            elif a[j] == 'M':
                minerals.append((i,j))
    flag1 = [[False for i in xrange(w)] for j in xrange(h)]
    dp1 = [[1e999 for i in xrange(w)] for j in xrange(h)]
    flag2 = [[False for i in xrange(w)] for j in xrange(h)]
    dp2 = [[1e999 for i in xrange(w)] for j in xrange(h)]
    
    #BFS For Mineral Patch 1
    q = [(minerals[1][0], minerals[1][1])]; dp1[minerals[1][0]][minerals[1][1]] = 0; flag1[minerals[1][0]][minerals[1][1]] = True;
    while len(q):
        u,v = q.pop(0)
        for x,y in (moves):
            x += u; y += v;
            if 0 <= x < h and 0 <= y < w:
                if not flag1[x][y]:
                    if graph[x][y] != 'W' and graph[x][y] != 'M':
                        flag1[x][y] = True
                        dp1[x][y] = dp1[u][v] + 1
                        q.append((x,y))
    
    #BFS For Mineral Patch 2
    q = [(minerals[0][0], minerals[0][1])]; dp2[minerals[0][0]][minerals[0][1]] = 0; flag2[minerals[0][0]][minerals[0][1]] = True;
    while len(q):
        u,v = q.pop(0)
        for x,y in (moves):
            x += u; y += v;
            if 0 <= x < h and 0 <= y < w:
                if not flag2[x][y]:
                    if graph[x][y] != 'W' and graph[x][y] != 'M':
                        flag2[x][y] = True
                        dp2[x][y] = dp2[u][v] + 1
                        q.append((x,y))
        
    #Actual BFS
    q = [probe]; flag[probe[0]][probe[1]] = True; dp[probe[0]][probe[1]] = 0;
    while len(q):
        u,v = q.pop(0)
        for x,y in moves:
            x += u; y += v;
            if 0 <= x < h and 0 <= y < w:
                if graph[u][v] == 'U':
                    if not flag[x][y]:
                        if graph[x][y] != 'M' and graph[x][y] != 'W':
                            if dp1[x][y] < dp1[u][v] or dp2[x][y] < dp2[u][v]:
                                flag[x][y] = True
                                q.append((x,y))
                                dp[x][y] = dp[u][v] + 1
                else:
                    if graph[x][y] != 'W' and graph[x][y] != 'M':
                        if not flag[x][y]:
                            if graph[x][y] == 'E' or graph[x][y] == 'C':
                                flag[x][y] = True
                                q.append((x,y))
                                dp[x][y] = dp[u][v] + 1
                            #    
                            elif graph[x][y] == 'U':
                                if dp1[x][y] < dp1[u][v] or dp2[x][y] < dp2[u][v]:
                                    flag[x][y] = True
                                    q.append((x,y))
                                    dp[x][y] = dp[u][v] + 1
        
    if dp[cannon[0]][cannon[1]] == 1e999:
        print 'terran so broken, apologize for playing this race'
    else:
        print 'pwned you in %s seconds eZ, learn to play n00b' % dp[cannon[0]][cannon[1]]
