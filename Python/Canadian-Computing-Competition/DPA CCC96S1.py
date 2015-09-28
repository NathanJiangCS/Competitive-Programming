a = input()
for i in range(a):
    b = input()
    divisors = []
    for i in range(1, int(b**0.5)+1):
        c = b % i
        if c == 0:
            d = b / i
            if d == b:
                divisors.append(i)
            else:
                if d not in divisors:
                    divisors.append(d)
                if i not in divisors:
                    divisors.append(i)

    x = sum(divisors)
    if x > b:
        print "%s is an abundant number." % b
    elif x == b:
        print "%s is a perfect number." % b
    else:
        print "%s is a deficient number." % b
