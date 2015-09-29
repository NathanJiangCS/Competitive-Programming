x = ['(',')','[',']','{','}','<','>']
for i in xrange(int(raw_input())):
    p = []
    b = list(raw_input())
    for i in b:
        if i in x:
            if not len(p):
                p.append(i)
            else:
                if i == ')':
                    if p[-1] == '(':
                        p = p[:-1]
                    else:
                        p.append(i)
                elif i == ']':
                    if p[-1] == '[':
                        p = p[:-1]
                    else:
                        p.append(i)
                elif i == '}':
                    if p[-1] == '{':
                        p = p[:-1]
                    else:
                        p.append(i)
                elif i == '>':
                    if p[-1] == '<':
                        p = p[:-1]
                    else:
                        p.append(i)
                else:
                    p.append(i)
    if len(p):
        print 'FALSE'
    else:
        print 'TRUE'
