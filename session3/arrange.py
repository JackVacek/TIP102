def arrange_guest_arrival_order(arrival_pattern):
    res = []
    stack = []
    for i in range(len(arrival_pattern) + 1):
        stack.append(i+1)
        
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                res.append(str(stack.pop()))
    return ''.join(res)


print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
