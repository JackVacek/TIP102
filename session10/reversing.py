'''
The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. 
Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Time complexity: O(N)
Space complexity: O(N)
'''
def helper(words,res):
    if not words:
        return ' '.join(res)
    return helper(words[1:], [words[0]] + res)
def reverse_orders(orders):
    return helper(orders.split(),[])
print(reverse_orders("Bagel Sandwich Coffee"))

'''
Initial function call

orders.split() → ["Bagel", "Sandwich", "Coffee"]

Calls reverse_orders_helper(["Bagel", "Sandwich", "Coffee"], 0, [])

First recursive call

index = 0, words[0] = "Bagel"

Result: ["Bagel"]

Calls reverse_orders_helper(["Bagel", "Sandwich", "Coffee"], 1, ["Bagel"])

Second recursive call

index = 1, words[1] = "Sandwich"

Result: ["Sandwich", "Bagel"]

Calls reverse_orders_helper(["Bagel", "Sandwich", "Coffee"], 2, ["Sandwich", "Bagel"])

Third recursive call

index = 2, words[2] = "Coffee"

Result: ["Coffee", "Sandwich", "Bagel"]

Calls reverse_orders_helper(["Bagel", "Sandwich", "Coffee"], 3, ["Coffee", "Sandwich", "Bagel"])

Base case reached

index = 3, which is the length of words

Returns ' '.join(["Coffee", "Sandwich", "Bagel"]) → "Coffee Sandwich Bagel"
'''