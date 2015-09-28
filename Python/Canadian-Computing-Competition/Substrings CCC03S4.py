import os
for t in xrange(int(raw_input())):
    a = raw_input()
    suffixes = []
    for i in xrange(len(a)):
        suffixes.append(a[i:])
    suffixes = sorted(suffixes)
    ans = len(suffixes[0])
    for i in xrange(len(suffixes)-1):
        LCP = [suffixes[i], suffixes[i+1]]
        an = len(os.path.commonprefix(LCP))
        ans += (len(LCP[1]) - an)
    print ans+1
        
