for zxc in range(input()):
    a = 1
    dictlist = []
    while a != '':
        string = ''
        a = raw_input()
        if a != '':
            a = a.split()
            for i in a:
                if i not in dictlist:
                    dictlist.append(i)
                    string += i
                else:
                    x = dictlist.index(i)
                    x = str(x+1)
                    string += x
                string += ' '
            print string.strip()
