'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Write a function next_greatest_letter() that returns the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.

Lexicographic order can also be defined as alphabetic order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
import bisect
def next_greatest_letter(letters, target):
    # a=bisect.bisect_right(letters, target)
    # return letters[a] if a < len(letters) else letters[0]
    l,r=0,len(letters)-1
    while l <= r:
        m=(l+r)//2
        if letters[m] <= target:
            l=m+1
        else:
            r=m-1
    return letters[l%len(letters)] 
letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))