for x in range(int(raw_input())):
    space = []
    a = list(raw_input())
    if len(a) == 4:
        g= "****"
    else:
        c = 0
        for i in range(len(a)):
            if a[i] == ' ':
                if c == 4:
                    space.append(i)
                c = 0
            else:
                c += 1
        c = 0
        for i in range(1, len(a)):
            if a[-i] != ' ':
               c += 1
            else:
                break
        if c == 4:
            a[-4:] = "****"
        
        for i in space:
            a[i-4:i] = '****'
        g = ''
        for i in range(len(a)):
            g = g+a[i]
    print g
    print 
