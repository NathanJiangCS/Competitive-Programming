for x in range(input()):
    a,b = map(int,raw_input().split('-'))
    lvl = (a-1)*4 + b
    #1-2 to 4-1 ### 4-2 to 8-1
    if lvl <= 2:
        print (2-lvl) + 7
    elif 2 < lvl <= 14:
        print (14-lvl) + 5
    else:
        print (32-lvl) + 1
