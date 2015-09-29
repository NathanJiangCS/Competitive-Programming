def floppy(x,y,c): # y = index
    if h == x:
        g.append(c)
    elif y == t:
        return (h-x)
    else:
        if (x + n[y]) > h:
            return floppy(x,y+1,c)
        else:
            return min(floppy(x,y+1,c),floppy(x+n[y], y+1,c+1))
h = int(raw_input())
t= int(raw_input())
n = []
g = []
for i in xrange(t):
    n.append(int(raw_input()))
floppy(0,0,0)
if g:
    print min(g)
else:
    print 0
