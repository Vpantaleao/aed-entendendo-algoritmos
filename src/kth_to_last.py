from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if not head:
        return -1
    if k == 0:
        return -1
    
    current = head
    runner = head
    for i in range(k):
        if runner is None:
            return -1
        runner = runner.next
        
    while runner is not None:
        current = current.next
        runner = runner.next

    return current.value


