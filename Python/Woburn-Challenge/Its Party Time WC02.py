def LCM(a,b): 
    if a * b == 0: 
        return 0 
    c = a 
    while (c % b) != 0: 
        c += a 
    return c

for zxc in range(input()):
    a,b,c = map(int,raw_input().split())
    d = LCM(b,c)
    print a + d
