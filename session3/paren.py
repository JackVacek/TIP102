def min_changes_to_make_balanced(schedule):
    stack = []
    minMoves = 0
    for i in schedule:
        if i == '(':
            stack.append(i)
        elif stack and i == ')':
            stack.pop()
        else:
            minMoves += 1
    return minMoves + len(stack)
    

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 