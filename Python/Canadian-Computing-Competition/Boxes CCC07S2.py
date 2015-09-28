boxes = []
for i in xrange(int(raw_input())):
    x= map(int,raw_input().split())
    boxes.append(sorted(x))
    
for i in xrange(int(raw_input())):
    a = sorted(map(int,raw_input().split()))
    b = a[0]; c = a[1]; d = a[2]
    best = 1e999
    for x,y,z in boxes:
        if b <= x:
            if c <= y:
                if d <= z:
                    if x*y*z < best:
                        best = x*y*z
    if best == 1e999:
        print 'Item does not fit.'
    else:
        print best
