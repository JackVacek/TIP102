def most_honey(height):
    l, r = 0, len(height)-1
    maxHoney = 0
    while l < r:
        maxHoney = max(maxHoney, min(height[l],height[r]) * (r - l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    print(maxHoney)
        

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)