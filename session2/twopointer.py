def reverse_list(lst):
    l = 0
    r = len(lst)-1
    while l < r:
        lst[l],lst[r] = lst[r],lst[l]
        l += 1
        r -= 1
    print(lst)

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)


#["eeyore", "roo", "piglet", "christopher robin", "pooh"]
