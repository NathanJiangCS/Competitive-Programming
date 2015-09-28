web = []
name = []
xz = input()
for i in range(xz):
    a = raw_input()
    a = a.strip()
    name.append(a)
    b = ''
    while a != '</HTML>':
        a = raw_input()
        a = a.strip()
        if a != '</HTML>':
            b += a   
    web.append(b)

adj = [[False for i in range(xz)] for j in range(xz)]
for i in range(xz):
    a =(web[i])
    b = a.count('A HREF')
    for j in range(b):
        c = (a.index('A HREF=') + 8)
        x = ''
        for k in range(c, len(a)):
            if a[k] != '"':
                x += a[k]
            else:
                break
        a = a.replace('A HREF', '', 1)
        print 'Link from %s to %s' % (name[i], x)
        if x in name:
            y = name.index(x)
            adj[i][y] = True
        
a = 1
while a != 'The End':
    a = raw_input()
    if a != 'The End':
        b = raw_input()
        a = a.strip()
        b = b.strip()
        x = name.index(a)
        y = name.index(b)

        flag = [False for i in range(xz)]
        flag[x] = True
        q = [x]
        while len(q):
            u = q.pop(0)
            for i in range(xz):
                if adj[u][i]:
                    if not flag[i]:
                        flag[i] = True
                        q.append(i)
        if flag[y]:
            print 'Can surf from %s to %s' % (a,b)
        else:
            print "Can't surf from %s to %s" % (a,b)
