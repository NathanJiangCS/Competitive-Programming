for zxc in xrange(5):
    red = 0
    grid = [['.' for j in xrange(6)] for i in xrange(7)]
    a = list(raw_input())
    win = False
    for i in xrange(42):
        if win:
            break
        b = int(a[i])
        b-= 1
        c = grid[b].index('.')
        if i % 2 == 0:
            grid[b][c] = 'r'
            red += 1
        else:
            grid[b][c] = 'b'
            red += 1
        if not win:
            #check horizonatal
            for j in xrange(6):
                for i in xrange(4):
                    if grid[i][j] != '.':
                        if grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j]:
                        
                            win = True
                            if grid[i][j] == 'r':
                                print 'RED-%s' % red
                            else:
                                print 'BLUE-%s' % red
        if not win:
            #check vertical
            for j in xrange(7):
                for i in xrange(2):
                    if grid[j][i] != '.':
                        if grid[j][i] == grid[j][i+1] == grid[j][i+2] == grid[j][i+3]:
                            win = True
                            if grid[j][i] == 'r':
                                print 'RED-%s' % red
                            else:
                                print 'BLUE-%s' % red
        if not win:
            for i in xrange(4):
                for j in xrange(3,6):
                    if grid[i][j] != '.':
                        if grid[i][j] == grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3]:
                            win = True
                            if grid[i][j] == 'r':
                                print 'RED-%s' % red
                            else:
                                print 'BLUE-%s' % red
        if not win:
            for i in xrange(4):
                for j in xrange(3):
                    if grid[i][j] != '.':
                        if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3]:
                            win = True
                            if grid[i][j] == 'r':
                                print 'RED-%s' % red
                            else:
                                print 'BLUE-%s' % red
