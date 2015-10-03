for zxc in range(int(raw_input())):
    hearts = '<3 '
    a = raw_input()
    for i in range(a.count('<3')):
        hearts += '<3 '
    print hearts.strip()
