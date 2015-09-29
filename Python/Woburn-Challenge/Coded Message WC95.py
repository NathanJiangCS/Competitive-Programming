for ix in xrange(5):
    
    a= raw_input()
    b = raw_input()
    while len(b) % 5 != 0:
        b += ' '
    chunks = len(b)/5
    if a == 'D':
        string = []
        for i in xrange(5):
            string.append(b[i*chunks:(i+1)*chunks])
        ans = ''
        for i in xrange(chunks):
            for j in xrange(5):
                ans += string[j][i]
        print ans
    else:
        string = ''
        for i in xrange(5):
            while i < len(b):
                string += b[i]
                i += 5
        print string    
