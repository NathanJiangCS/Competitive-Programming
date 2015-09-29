def bases(a, b):
    x = ''
    while a > 0:
        x = str(a % b)+x
        a /= b
    return x

for z in range(int(raw_input())):
    a = int(raw_input())
    if a == 0:
        print 0
    else:
        a = bases(a, 2)
        a = a[::-1]
        a = int(a, 2)
        print a
