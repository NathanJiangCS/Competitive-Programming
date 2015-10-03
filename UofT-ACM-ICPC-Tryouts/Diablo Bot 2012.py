def sets(x): #If it has 's, it is for sure a set item
    zxc = x.split()[0]
    if zxc[-1] == 's' and zxc[-2] == "'":
        return True
    else:
        return False
      
def rare(x): #Has names that are 2 words long
    split = x.split()
    if len(split) == 2:
        return True
    else:
        return False

def magic(x): #Has 2-4 words in name. If it has more than 2, then the last 2 words are of[something]
    splits = x.split()
    if 2 <= len(splits) <= 4:
        if len(splits) != 2:
            if splits[-2] == 'of':
                return True
            else:
                return False
        else:
            if splits[-2] == 'of':
                return False
            else:
                return True
    else:
        return False
def normal(x):
    spli = x.split()
    if spli[0] == 'damaged':
        return True
    else:
        return False

for i in range(input()):
    name = raw_input().lower()
    words = len(name.split())
    s = sets(name)
    r = rare(name)
    m = magic(name)
    n = normal(name)

    if s:
        print 'Set'
    elif r and m and not n:
        print 'Not sure, take anyways'
    elif n:
        print 'Normal'
    elif m:
        print 'Magic'
    elif r:
        print 'Rare'
    elif not r and not m and not s:
        print 'Normal'
