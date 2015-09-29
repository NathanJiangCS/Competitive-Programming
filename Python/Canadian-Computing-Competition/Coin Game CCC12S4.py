n = 1
while n != 0:
    n =int(raw_input())
    if n != 0:
        if n == 1:
            asd = map(int,raw_input().split())
            print 0
        else:
            final = [() for i in xrange(n)]
            for i in xrange(1,n+1):
                final[i-1] += (i,)
            final = tuple(final)
                
            a = [() for i in xrange(n)]
            b = map(int,raw_input().split())
            for i in xrange(len(b)):
                a[i] += (b[i],)
            a = tuple(a)
            
            flag = set()
            flag.add(a)
            q = [(a,0)]
            possible = False

            
            while len(q):
                k, count = q.pop(0)
                if k == final:
                    print count
                    possible = True
                    q = []
                    break
                for i in xrange(n):
                    if len(k[i]):
                        u = k
                        if i-1 >= 0:
                            if len(u[i-1]):
                                if u[i-1][-1] > u[i][-1]:
                                    u = list(u)
                                    a = u[i][-1]
                                    c = u[i][:-1]
                                    u[i] = c
                                    u[i-1]+=(a,)
                                    u = tuple(u)
                                    if u not in flag:
                                        flag.add(u)
                                        q.append((u,count+1))
                                        
                            else:
                                u = list(u)
                                a = u[i][-1]
                                c = u[i][:-1]
                                u[i] = c
                                u[i-1]+=(a,)
                                u = tuple(u)
                                if u not in flag:
                                    flag.add(u)
                                    q.append((u,count+1))
                                
                        u = k
                        if i+1<n:
                            if len(u[i+1]):
                                if u[i+1][-1] > u[i][-1]:
                                    u = list(u)
                                    a = u[i][-1]
                                    c = u[i][:-1]
                                    u[i] = c
                                    u[i+1] += (a,)
                                    u = tuple(u)
                                    if u not in flag:
                                        flag.add(u)
                                        q.append((u,count+1))
                                    
                            else:
                                u = list(u)
                                a = u[i][-1]
                                c = u[i][:-1]
                                u[i] = c
                                u[i+1] += (a,)
                                u = tuple(u)
                                if u not in flag:
                                    flag.add(u)
                                    q.append((u,count+1))
                                                      
                        
            if not possible:
                print "IMPOSSIBLE"
