#Write a function linear_search() to help Winnie the Pooh locate his lost items. 
# The function accepts a list items and a target value as parameters. 
# The function should return the first index of target in items, 
# and -1 if target is not in the lst. Do not use any built-in functions.

def linear_search(lst, target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i
            break
    return index
            

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'haycorn'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']

target = 'red balloon'
print(linear_search(items, target))