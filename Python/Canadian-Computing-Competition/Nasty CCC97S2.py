def factors(x):
    for i in xrange(1, int(x ** 0.5)+1):
        if x % i == 0:
            t = x / i
            facts.append(t+i)
            facts.append(t-i)

for zxc in xrange(int(raw_input())):
    a = int(raw_input())
    facts = []
    factors(a)
    facts = sorted(facts)
    nasty = False
    for i in facts:
        if facts.count(i) == 2:
            nasty = True
            break
    if nasty:
        print '%s is nasty' % a
    else:
        print '%s is not nasty' % a
