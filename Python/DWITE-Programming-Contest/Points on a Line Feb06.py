points = []
for i in xrange(int(raw_input())):
    a,b = map(int,raw_input().split())
    points.append((a,b))
for zxc in xrange(5):
    x1,y1,x2,y2 = map(int,raw_input().split())
    count = 0
    if x2 - x1 == 0:
        for i,j in points:
            if i == x2:
                count += 1
    elif y2 - y1 == 0:
        for i,j in points:
            if j == y2:
                count += 1
    else:
        slope = (y2-y1)/(float(x2)-float(x1))
        intercept = y2-(slope*x2)
        for i,j in points:
            if j == i*slope + intercept:
                count += 1
    print count
