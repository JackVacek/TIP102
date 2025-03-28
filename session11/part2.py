def helper(l,r,inventory,part_id):
    if l > r:
        return False
    m=(l+r)//2
    if inventory[m] == part_id:
        return True
    elif inventory[m] > part_id:
        return helper(m+1,r,inventory,part_id)
    else:
        return helper(l,m-1,inventory,part_id)

def check_stock(inventory, part_id):
    return helper(0,len(inventory),inventory,part_id)

print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100))