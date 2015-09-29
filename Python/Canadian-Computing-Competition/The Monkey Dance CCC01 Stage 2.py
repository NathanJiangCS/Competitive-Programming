def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

a = 1

while a != 0:
    a = int(raw_input())
    if a != 0:
        d = [-1 for x in xrange(a)]
        checked = [False for i in xrange(a)]
        cycles = []
        for i in xrange(a):
            b,c = map(int,raw_input().split())
            b -= 1; c -= 1
            d[b] = (c)

        for i in xrange(a):
            if not checked[i]:
                q = d[i]
                checked[i] = True
                checked[q] = True
                c = 1
                while q != i:
                    q = d[q]
                    checked[q] = True
                    c += 1
                cycles.append(c)
        while len(cycles) != 1:
            x = cycles[0]; y = cycles[1]
            del cycles[1]; del cycles[0]
            cycles.append((x * y) / gcd(x,y))
        print cycles[0]
