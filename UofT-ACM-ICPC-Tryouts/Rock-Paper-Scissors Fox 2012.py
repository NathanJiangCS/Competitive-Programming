b = []
for i in range(int(raw_input())):
    a = raw_input()
    if a == 'Scissors':
        b.append( 'Rock')
    elif a == 'Rock':
        b.append( 'Paper')
    elif a == 'Paper':
        b.append( 'Scissors')
    elif a == 'Fox':
        b.append( 'Foxen')
    else:
        b.append(1)
        
for i in b:
    if i != 1:
        print i
    else:
        break
