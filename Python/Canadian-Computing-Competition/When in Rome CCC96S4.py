roman = {1:'I', 4:'IV', 5:'V', 9:'IX',10:'X',40:'XL',50:'L', 90:'XC', 100:'C', 400: 'CD',500:'D', 900: 'CM', 1000: 'M'}
numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
pos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def integers_to_numerals(x):
    if x in numbers:
        return roman[x]
    else:
        string = ''
        for i in numbers:
            while x-i >= 0:
                x -= i
                string += roman[i]
        return string

def numerals_to_integers(x):
    x = x[::-1]
    a = []
    for i in x:
        a.append(pos[i])
    total = 0
    m = 0
    for i in a:
        if i >= m:
            total += i
            m = i
        else:
            total -= i
    return total
for i in xrange(int(raw_input())):
    g = raw_input()
    plus = g.index('+')
    equal = g.index('=')
    first = g[:plus]
    second = g[plus+1:equal]
    first = numerals_to_integers(first)
    second = numerals_to_integers(second)
    tot = first + second
    if tot > 1000:
        print (g+'CONCORDIA CUM VERITATE')
    else:        
        ans = integers_to_numerals(tot)
        print (g+ans)
