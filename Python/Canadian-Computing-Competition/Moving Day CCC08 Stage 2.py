names = {}
graph = [[] for i in xrange(101)]
degrees = [-1 for i in xrange(101)]
s = []
l = []
for i in xrange(int(raw_input())):
    a,b,c = raw_input().split(); b = int(b); c = int(c);
    graph[b].append(c)
    names[b] = a
    
    if degrees[b] == -1:
        degrees[b] = 0
        
    if degrees[c] == -1:
        degrees[c] = 1
    else:
        degrees[c] += 1
        
for i in xrange(101):
    if degrees[i] == 0:
        s.append(i)

while s:
    n = s.pop(0)
    l.append(n)
    for i in graph[n]:
        degrees[i] -= 1
        if degrees[i] == 0:
            s.append(i)
l = l[::-1]
for i in degrees:
    if i > 0:
        print 'Impossible'
        quit()
        
for i in xrange(len(l)):
    if l[i] in names:
        print names[l[i]]
        
