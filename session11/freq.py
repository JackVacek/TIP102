import bisect
def find_frequency_positions(transmissions, target_code):
    # a=bisect.bisect_left(transmissions,target_code)
    # b=bisect.bisect_right(transmissions,target_code)
    # if a < 0 or a > len(transmissions) or b-1 < 0 or b-1 > len(transmissions):
    #     return (-1,-1)
    # return (a,b-1) if transmissions[a] == target_code and transmissions[b-1] == target_code else (-1,-1)
    l,r=0,len(transmissions)-1
    curr=-1
    while l <= r:
        m=(r+l)//2
        if transmissions[m]==target_code:
            curr=m
            r=m-1
        elif transmissions[m]>target_code:
            r = m - 1
        else:
            l = m + 1      
    l,r=0,len(transmissions)-1
    curr2=-1
    while l <= r:
        m=(r+l)//2
        if transmissions[m]==target_code:
            curr2=m
            l=m+1
        elif transmissions[m]>target_code:
            r = m - 1
        else:
            l = m + 1
    return (curr,curr2) if curr != -1 and curr2 != -1 else (-1,-1)
print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))