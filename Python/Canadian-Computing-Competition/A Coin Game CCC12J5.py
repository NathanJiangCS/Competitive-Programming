from copy import deepcopy
n = 1
while n != 0:
    n =int(raw_input())
    if n != 0:
        if n == 1:
            asd = map(int,raw_input().split())
            print 0
        else:
            final = [[] for i in xrange(n)]
            for i in xrange(1,n+1):
                final[i-1].append(i)
                
            a = [[] for i in xrange(n)]
            b = map(int,raw_input().split())
            for i in xrange(len(b)):
                a[i].append(b[i])
            flag = [a]
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
                        u = deepcopy(k)
                        if i-1 >= 0:
                            if len(u[i-1]):
                                if u[i-1][-1] > u[i][-1]:
                                    a = u[i][-1]
                                    del u[i][-1]
                                    u[i-1].append(a)
                                    if u not in flag:
                                        flag.append(u)
                                        q.append((u,count+1))
                                        
                            else:
                                a = u[i][-1]
                                del u[i][-1]
                                u[i-1].append(a)
                                if u not in flag:
                                    flag.append(u)
                                    q.append((u,count+1))
                                
                        u = deepcopy(k)
                        if i+1<n:
                            if len(u[i+1]):
                                if u[i+1][-1] > u[i][-1]:
                                    a = u[i][-1]
                                    del u[i][-1]
                                    u[i+1].append(a)
                                    if u not in flag:
                                        flag.append(u)
                                        q.append((u,count+1))
                                    
                            else:
                                a = u[i][-1]
                                del u[i][-1]
                                u[i+1].append(a)
                                if u not in flag:
                                    flag.append(u)
                                    q.append((u,count+1))
                                                      
                        
            if not possible:
                print "IMPOSSIBLE"
