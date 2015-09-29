for i in xrange(5):
    n = int(raw_input())
    d = [0 for i in xrange(n-1)]
    x = y = a = b = 1
    z = 0
    while x != 0 or y != 0 or a != 0 or b != 0:
        x,y,a,b = map(int,raw_input().split())
        if x != 0 or y != 0 or a != 0 or b != 0:  
            a -= 1; b -= 1
            if a == 0:
                z += 1
            if 0 <= a-1 < n-1:
                d[a-1] += 1
            if 0 <= b < n-1:
                d[b] -= 1
    fish = [z]
    for i in d:
        z += i
        fish.append(z)
    print fish.index(max(fish))+1
