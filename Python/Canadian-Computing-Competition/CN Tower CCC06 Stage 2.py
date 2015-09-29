from math import ceil
times = []
for zxc in xrange(int(raw_input())):
    name, x = raw_input().split()
    x =  float(x)
    x = round(x* 12, 15)
    times.append(x)
dif = []
times = sorted(times)
for i in xrange(1,len(times)):
    dif.append(round(4320.0- times[i] + times[i-1],15))
dif.append(round(times[-1] - times[0], 15))
g = int(min(dif))
if float(g) == round(min(dif),10):
    print int(min(dif))
else:
    print int(ceil(min(dif)))
