#import sys
#sys.stdin = open('test.txt','r')
tiles = input()
rows = input()
columns = input()
roomsizes = []
adj = [[False for i in xrange(columns)] for j in xrange(rows)]
flag = [[False for i in xrange(columns)] for j in xrange(rows)]
for i in range(rows):
    a = raw_input()
    for j in range(columns):
        if a[j] == '.':
            adj[i][j] = True
moves = [[0,1],[1,0],[0,-1],[-1,0]]            
for y in range(len(adj)):
    for x in range(len(adj[y])):
        if adj[y][x] == True:
            if flag[y][x] == False:
                q = [[y,x]]
                room = 0
                while len(q) > 0:
                    y1,x1 = q.pop(0)
                    for i in moves:
                        a,b = i
                        a += x1
                        b += y1
                        if 0 <= a <= (columns-1) and 0 <= b <= (rows-1):
                            if adj[b][a] == True:
                                if flag[b][a] == False:
                                    q.append([b,a])
                                    flag[b][a] = True
                                    room += 1
                if room == 0:
                    room = 1
                roomsizes.append(room)
roomsizes = sorted(roomsizes)
roomsizes.reverse()
rooms = 0
for i in roomsizes:
    if tiles - i >= 0:
        tiles -= i
        rooms += 1
    else:
        break
if rooms != 1:
    print '%s rooms, %s square metre(s) left over' % (rooms, tiles)
else:
    print '%s room, %s square metre(s) left over' % (rooms, tiles)   
