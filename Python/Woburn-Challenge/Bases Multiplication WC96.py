def bases(a, b):
    x = ''
    while a > 0:
        x = str(a % b)+x
        a /= b
    return x

for zxc in range(5):
    a,abase = map(int,raw_input().split())
    b,bbase = map(int,raw_input().split())
    a = int(str(a),abase)
    b = int(str(b),bbase)
    fbase = input()
    c = a * b
    c = bases(c, fbase)
    print c
