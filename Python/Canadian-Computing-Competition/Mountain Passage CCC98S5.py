for zxc in xrange(input()):
    size = input()
    graph = []
    oxy = [[1e999 for i in xrange(size)] for j in xrange(size)]
    for i in xrange(size):
        line = []
        for j in xrange(size):
            line.append(input())
        graph.append(line)

    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    oxy[0][0] = 0
    h = graph[0][0]

    q = [[0,0]]
    while len(q):
        a,b = q.pop(0)
        for x,y in moves:
            x += a
            y += b
            if 0 <= x < size and 0 <= y < size:
                if -2 <= graph[y][x] - graph[b][a] <= 2:            
                    if graph[b][a] >  h or graph[y][x] > h:
                        t = 1
                    else:
                        t = 0
                    if oxy[b][a] + t < oxy[y][x]:
                        oxy[y][x] = oxy[b][a] + t
                        q.append([x,y])
    if oxy[size-1][size-1] == 1e999:
        print 'CANNOT MAKE THE TRIP'
    else:
        print oxy[size-1][size-1]
