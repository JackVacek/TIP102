'''
You are an architect designing a corridor for a futuristic dream space.
The corridor is represented by a list of integer values where each value represents the width of a segment of the corridor.
Your goal is to find two segments such that the corridor formed between them (including the two segments) has the maximum possible area. 
The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.
'''

def max_corridor_area(segments):
    l, r = 0, len(segments)-1
    biggest = 0
    while l < r:
        biggest = max(biggest, min(segments[l],segments[r]) * (r - l))
        if segments[l] <= segments[r]:
            l += 1
        else:
            r -= 1
    return biggest

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 