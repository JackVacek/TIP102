class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    ph = head
    while head.next:
        head = head.next
    head.next = Node(new_fish)
    return ph

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))
