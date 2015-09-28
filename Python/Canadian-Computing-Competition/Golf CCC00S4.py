amount = int(raw_input())
num = int(raw_input())
dist = []
mindist = [1e999 for i in range(amount+1)]
mindist[0] = 0
for i in range(num):
    dist.append(int(raw_input()))
for i in range(len(mindist)):
    for j in range(num):
        if dist[j] <= i:
            mindist[i] = min(mindist[i], (1+mindist[i-dist[j]]))
if mindist[amount] == 1e999:
    print 'Roberta acknowledges defeat.'
else:
    print 'Roberta wins in %s strokes.' % mindist[amount]
