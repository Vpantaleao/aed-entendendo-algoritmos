from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if not head:
        return False
    
    turtle = head
    hare = head

    while hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next

        if turtle == hare:
            return True
    
    return False
