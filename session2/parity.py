'''
Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
'''

def sort_by_parity(nums):
    even = [i for i in nums if i % 2 == 0]
    odd = [i for i in nums if i % 2 == 1]
    ans = []
    for i in even:
        ans.append(i)
    for i in odd:
        ans.append(i)
    print(ans)

nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)