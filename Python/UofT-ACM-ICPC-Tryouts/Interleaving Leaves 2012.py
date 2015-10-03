a = int(raw_input())
for i in range(a):
    final = ''
    b = int(raw_input())
    pile1 = raw_input()
    pile2 = raw_input()
    for i in range(b):
        final = final + pile1[i]
        final = final + pile2[i]
    print final[::-1]
