for x in range(5):
    d = 0
    for i in range(3):
        a = input()
        b = input()
        c = (1 - (b / a)) * 100
        if c > d:
            d = c
    string = '%.3f' % d
    string = string.rjust(7)
    print string
