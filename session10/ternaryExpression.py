def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    pass

print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))