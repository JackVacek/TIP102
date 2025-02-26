from collections import Counter
def funct(arr):
    return dict(Counter(arr))

arr = ['apple','banana','apple','orange','banana','apple']
print(funct(arr))