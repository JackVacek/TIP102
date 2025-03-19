class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    current = dna_strand
    while current:
        for i in range(1, m):
            if current is None:
                return dna_strand
            current = current.next
        if current is None:
            return dna_strand
        temp = current.next
        for j in range(n):
            if temp is None:
                break
            temp = temp.next
        current.next = temp
        current = temp

    return dna_strand

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))