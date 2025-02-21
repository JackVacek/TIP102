'''
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. 
Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.
'''

def remove_dupes(items):
    st = set()
    length = len(items)
    for i in items:
        if i in st:
            length -= 1
        st.add(i)
    print(length)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)

'''
4
4
'''