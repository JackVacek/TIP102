class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    temp = Node(0) 
    temp.next = head
    prev = temp
    curr = head
    while curr:
        while curr.next and curr.value == curr.next.value:
            curr = curr.next
        if prev.next == curr:
            prev = prev.next
        else:
            prev.next = curr.next
        curr = curr.next
    return temp.next
        
            

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

print_linked_list(delete_dupes(head))