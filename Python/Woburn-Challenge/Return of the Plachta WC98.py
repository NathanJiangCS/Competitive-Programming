def factor(x, y):
    remainder = 1
    while remainder != 0:
        remainder = x % y
        x = y
        y = remainder
    return x
for x in range(5):
    an, ad, bn, bd = map(int, raw_input().split())
    if an == 0 and bn == 0:
        print 0
    else:
        num = (an * bd) + (bn * ad)
        den = ad * bd
        if num == den:
            print 1
        elif num > den:
            gcf = factor(num, den)
            num = num / gcf
            den = den / gcf
            if den == 1:
                print num
            else:
                print num, den

        else:
            gcf = factor(den, num)
            num = num / gcf
            den = den / gcf
            if den == 1:
                print num
            else:
                print num, den
