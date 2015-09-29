a = raw_input()
totalsum = 0
past = 9999
pastadd = 0
for i in range(0, len(a)/2):
    i1 = i * 2
    i2 = i1 + 1
    x = int(a[i1])
    y = a[i2]
    if y == 'I':
        y = 1
    elif y =='V':
        y = 5
    elif y =='X':
        y = 10
    elif y =='L':
        y = 50
    elif y =='C':
        y = 100
    elif y =='D':
        y = 500
    elif y =='M':
        y = 1000
    if y <= past:
        past = y
        totalsum += pastadd
        pastadd = x * y
    else:
        past = y
        totalsum -= pastadd
        pastadd = x*y
y = a[-1]
if y == 'I':
    y = 1
elif y =='V':
    y = 5
elif y =='X':
    y = 10
elif y =='L':
    y = 50
elif y =='C':
    y = 100
elif y =='D':
    y = 500
elif y =='M':
    y = 1000
x = int(a[-2])
totalsum += (x * y)
print totalsum
