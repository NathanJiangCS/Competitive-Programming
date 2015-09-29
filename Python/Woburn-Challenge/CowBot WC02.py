def isprime(n):
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False
      i += w
      w = 6 - w
   return True

def prime(x):
    if isprime(x):
        x = x * 11
        return x, True
    return x, False

def ps(x):
    y = x ** 0.5
    if (int(y) ** 2 == x):
        x = str(x)
        y = x[::-1]
        x, y = int(x), int(y)
        x = x + y
        return int(x), True
    return x, False
   
def palindrome(x):
    x = str(x)
    if x == x[::-1]:
        x = x + '4'
        return int(x), True
    return int(x), False
   
def sw2(x):
    x = str(x)
    if x[0] == '2':
        x = '5' + x
        return int(x), True
    return int(x), False
   
def seven(x):
    x = str(x)
    if '7' in x:
        x = x[:len(x)-1]
        return int(x), True
    return int(x),False
def six(x):
    if x % 6 == 0:
        x = str(x)
        x = x[1:]
        return int(x), True
    return int(x), False
def even(x):
    x = str(x)
    if len(x) % 2 == 0:
        x = x[:len(x)/2] + '1' + x[len(x)/2:]
        return int(x), True
    return int(x), False
def odd(x):
    x = str(x)
    if len(x) % 2 == 1:
        x = int(x)
        x += 231
        return x
    return int(x)

for zxc in range(input()):
    a,b = map(int,raw_input().split())
    for i in range(b):
       z = False
       a,z = prime(a)
       if z == False:
          a,z = ps(a)
       if z == False:
          a,z = palindrome(a)
       if z == False:
          a,z = sw2(a)
       if z == False:
          a,z = seven(a)
       if z == False:
          a,z = six(a)
       if z == False:
          a,z = even(a)
       if z == False:
          a = odd(a)


    print a
