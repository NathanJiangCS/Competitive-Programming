def floppy(x,y): # y = index
    if y == t:
        return (1440-x)
    else:
        if (x + n[y]) > 1440:
            return floppy(x,y+1)
        else:
            return min(floppy(x,y+1),floppy(x+n[y], y+1))
for i in xrange(5):
    t = int(raw_input())
    n = [int(raw_input()) for i in xrange(t)]
    print floppy(0,0)
