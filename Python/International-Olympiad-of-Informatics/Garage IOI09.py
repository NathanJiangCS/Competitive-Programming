ps, cc = map(int,raw_input().split())
spaces = []
cars = []
for i in range(ps):
    spaces.append([input(),False, -1])
for i in range(cc):
    cars.append(input())
price = 0
q = []
for i in range(2*cc):
    x = input()
    if x > 0:
        x -= 1
        q.append(x)
        for j in range(ps):
            if not spaces[j][1]:
                x = q.pop(0)
                spaces[j][1] = True
                price = price + (spaces[j][0] * cars[x])
                spaces[j][2] = x
                break
    else:
        x = (x* -1) -1
        for j in range(ps):
            if spaces[j][2] == x:
                spaces[j][2] = -1
                spaces[j][1] = False
                break
            
        if len(q):
            x = q.pop(0)
            for j in range(ps):
                if not spaces[j][1]:
                    spaces[j][1] = True
                    price = price + (spaces[j][0] * cars[x])
                    spaces[j][2] = x
                    break

print price
