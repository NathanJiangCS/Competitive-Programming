maxweight = int(raw_input())
trains = []
c = 0
success = True
y = int(raw_input())
for i in range(y):
    x = int(raw_input())
    trains.append(x)
    if len(trains) > 4:
        del trains[0]
    if sum(trains) > maxweight:
        print c
        success = False
        break
    else:
        c+= 1
        
            
if success:
    print y
