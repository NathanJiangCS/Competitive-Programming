from copy import deepcopy
a,b = raw_input().split()
a = int(a)
b = int(b)
area = [[] for i in xrange(a)]
neighbour = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
for i in xrange(a):
    line = raw_input()
    for j in line:
        area[i].append(j)

for zxc in xrange(100):
    newarea = deepcopy(area)
    for i in xrange(a):
        for j in xrange(b):
            dead = 0
            live = 0
            cell = newarea[i][j]
            for k in neighbour:
                ma,mb = k
                if 0 <= (i+ma) < (a) and 0 <= (j +mb) < (b):
                    if area[i+ma][j+mb] == 'X':
                        live += 1
                    else:
                        dead += 1
            if cell == '.' and live == 3:
                newarea[i][j] = 'X'
            elif cell == 'X' and live == 2 or live == 3:
                newarea[i][j] = 'X'
            elif cell == 'X' and live <= 1 or live >= 4:
                newarea[i][j] = '.'

    area = deepcopy(newarea)
    if zxc == 0 or zxc == 4 or zxc == 9 or zxc == 49 or zxc == 99:
        count = 0
        for i in xrange(a):
            for j in xrange(b):
                if area[i][j]== 'X':
                    count += 1
        print count
                        
