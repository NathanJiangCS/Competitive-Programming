dp = [99999 for i in xrange(50)]
adj = [[False for i in xrange(50)] for j in xrange(50)]
flag = [False for i in xrange(50)]
adj[0][5] = adj[5][0] = adj[5][1] = adj[1][5] = adj[5][6]  = adj[6][5]  = adj[2][5] = adj[5][2] = adj[3][5]  = adj[5][3] = adj[4][5] = adj[5][4] = adj[2][3] = adj[3][2] = adj[2][4] = adj[4][2] = adj[3][4] = adj[4][3] = adj[6][7] = adj[7][6] = adj[7][8] = adj[8][7] = adj[8][9] = adj[9][8] = adj[11][8] = adj[8][11] = adj[10][9] = adj[9][10] = adj[10][11] = adj[11][10] = adj[2][14] = adj[14][2] = adj[14][12] = adj[12][14] = adj[11][12] = adj[12][11] = adj[13][12] = adj[12][13] = adj[15][16] = adj[16][15] = adj[16][17] = adj[17][16] = adj[15][17] = adj[17][15] = True

while 1:
    a = raw_input()
    if a == 'i':
        x = input()
        y = input()
        adj[x-1][y-1] = True
        adj[y-1][x-1] = True
    elif a =='d':
        x = input()
        y = input()
        adj[x-1][y-1] = False
        adj[y-1][x-1] = False
    elif a == 'n':
        x = input()
        c = 0
        for i in adj[x-1]:
            if i == True:
                c += 1
        print c
    elif a == 'f':
        x = input()
        c = []
        for i in range(50):
            if adj[x-1][i] == True:
                c.append(i)
        d = []
        for i in c:
            for j in range(50):
                if adj[i][j] == True:
                    d.append(j)
        for i in c:
            if i in d:
                for j in range(d.count(i)):
                    d.remove(i)
        d = list(set(d))
        for i in range(d.count(x-1)):
            d.remove(x-1)
        print len(d)
                
    elif a == 's':
        x = input()
        y = input()
        dp[(x-1)] = 0
        q = [(x-1)]
        while len(q) > 0:
            u = q.pop(0)
            for i in range(50):
                if adj[u][i]:
                    if flag[i] == False:
                        flag[i] = True
                        q.append(i)
                        dp[i] = (dp[u] + 1)
        if dp[y-1] == 99999:
            print 'Not connected'
        else:
            print dp[y-1]
        flag = [False for i in xrange(50)]
        dp = [99999 for i in xrange(50)]
    else:
        quit()
