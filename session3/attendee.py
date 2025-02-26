from collections import deque
def reveal_attendee_list_in_order(attendees):
    attendees = sorted(attendees, reverse=True)
    q = deque([])
    for i in attendees:
        if q:
            q.appendleft(q.pop())
        q.appendleft(i)
    return list(q)
    
           

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  