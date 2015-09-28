from itertools import combinations
cookies = []
for i in xrange(int(raw_input())):
    a,b = map(int,raw_input().split())
    cookies.append((a,b))
d = list(combinations(cookies,3))
m=0
for x,y,z in d:
    x1 = x[0]; y1 = x[1]
    x2 = y[0]; y2 = y[1]
    x3 = z[0]; y3 = z[1]
    a = float(((x2-x1)**2 + (y2-y1)**2)**0.5)
    b = float(((x3-x2)**2 + (y3-y2)**2)**0.5)
    c = float(((x3-x1)**2 + (y3-y1)**2)**0.5)
    if a > m:
        m =a
    if b > m:
        m =b
    if c > m:
        m = c
    semi = (a+b+c)/2
    if semi==0 or semi==a or semi==b or semi==c or (a**2 + b**2 - c**2 < 0) or (b**2 + c**2 - a**2 < 0) or (a**2 + c**2 - b**2 < 0):
        if a>m:
            m = a
            m = b
        if c>m:
            m = c
    else:
        g = 2*(a*b*c)/(4*(semi * (semi - a) * (semi - b) * (semi - c))**0.5)
        if g > m:
            m = g
print "%.2f" %m
