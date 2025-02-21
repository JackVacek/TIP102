def batman(n):
    lst = []
    for i in range(n):
        lst.append('na')
    if n > 0:
        lst.append(' ')
    lst.append('batman')
    print(''.join(lst))

batman(0)
batman(5)