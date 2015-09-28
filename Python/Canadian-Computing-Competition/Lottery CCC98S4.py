for zxc in xrange(int(raw_input())):
    a = raw_input().split()
    n = len(a)
    ans = []; fans = []
    i = 0
    while i< n:
        if a[i] == 'X':
            k = ans.pop()
            ans.append('(' + k + ' X ' + a[i+1] + ')')
            i += 2
        else:
            ans.append(a[i])
            i += 1
    n = len(ans)
    i = 0
    while i<n:
        if ans[i] == '+':
            k = fans.pop()
            fans.append('(' + k + ' + ' + ans[i+1] + ')')
            i += 2
        elif ans[i] == '-':
            k = fans.pop()
            fans.append('(' + k + ' - ' + ans[i+1] + ')')
            i += 2
        else:
            fans.append(ans[i])
            i += 1
    print fans[0][1:-1]
