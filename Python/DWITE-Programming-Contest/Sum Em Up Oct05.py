for x in range(5):
    number = []
    a,b = map(int, raw_input().split())
    c = 0
    if a > b:
        for i in range(b, a + 1):
            number.append(i)
            c += i
    else:
        for i in range(a, b + 1):
            number.append(i)
            c += i
    string = ''
    for i in range(len(number)):
        number[i] = str(number[i])
        if i == len(number)- 1:
            string += number[i] + '='
        else:
            string += number[i] + '+'
    print (string + str(c))
