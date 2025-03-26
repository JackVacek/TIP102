'''
A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. 
Given the heads of two linked lists sandwich_a and sandwich_b where each node in the lists contains a spell segment, write a recursive function merge_orders() 
that merges the two sandwiches together in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

Return the head of the merged sandwich.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Time complexity: O(N)
Space complexity: O(N)
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a and not sandwich_b:
        return None
    if not sandwich_b:
        return sandwich_a
    if not sandwich_a:
        return sandwich_b
    nextA=sandwich_a.next
    nextB=sandwich_b.next
    sandwich_a.next=sandwich_b
    sandwich_b.next=merge_orders(nextA,nextB)
    return sandwich_a
    

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))
