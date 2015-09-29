a = int(raw_input())
ppl1 = raw_input().split()
ppl2 = raw_input().split()
partners = []
for i in range(a):
    partners.append([ppl1[i],ppl2[i]])

for i in range(len(partners)):
    partners[i] = sorted(partners[i])

partners = sorted(partners)

bad = False
for i in partners:
    if partners.count(i) != 2:
        print 'bad'
        bad = True
        break
if not bad:
    print 'good'
