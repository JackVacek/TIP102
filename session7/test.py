from collections import Counter
def findDup(arr):
    return([c for c,v in Counter(arr).items() if v > 1])
print(findDup(['a','a','b','b','b','c']))