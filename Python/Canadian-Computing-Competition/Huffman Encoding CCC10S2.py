letters = {}
for zxc in xrange(int(raw_input())):
    l, c = raw_input().split()
    letters[c] = l
s = list(raw_input())
t = ''
ans = ''
for i in s:
    t += i
    if t in letters:
        ans += letters[t]
        t = ''
print ans
