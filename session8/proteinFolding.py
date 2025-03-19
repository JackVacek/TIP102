class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    if not protein:
        return []
    slow = protein
    fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return []
    slow = protein
    while slow != fast:
        slow = slow.next
        fast = fast.next
    cycle_nodes = []
    start_of_cycle = slow
    while True:
        cycle_nodes.append(slow.value)
        slow = slow.next
        if slow == start_of_cycle:
            break
    return cycle_nodes

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))