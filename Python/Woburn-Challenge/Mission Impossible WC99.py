a=1;b=1
moves = [[0,1],[1,0],[0,-1],[-1,0]] 
while a != -1 and b != -1:
    tt = raw_input().strip()
    a,b = map(int,tt.split())
    if a != -1 and b != -1:
        count = 0
        adj = [[False for i in xrange(a)] for j in xrange(b)]
        for i in xrange(b):
            x = raw_input()
            for j in range(len(x)):
                if x[j] != '0':
                    adj[i][j] = True
        
        for i in xrange(b):
            for j in xrange(a):
                if adj[i][j]:
                    count += 1
                    adj[i][j] = False
                    q = [[i,j]]
                    while len(q):
                        u = q.pop(0)
                        i,j = u
                        for zxc in moves:
                            x1,y1 = zxc
                            x1 += i
                            y1 += j
                            if 0 <= x1 <= (b-1) and 0 <= y1 <= (a-1):
                                if adj[x1][y1]:
                                    q.append([x1,y1])
                                    adj[x1][y1] = False
                    
        print count
