class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycle:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        marker = curr = head
        curr = curr.next
        while curr.next.next:
            if marker is curr:
                return True
            marker = marker.next
            curr = curr.next.next
        return False


class Test:
    test = LinkedListCycle()
    head = ListNode(1)
    curr = head.next = ListNode(2)
    temp = curr
    for i in range(3, 10):
        curr.next = ListNode(i)
        curr = curr.next
    curr.next = temp

    print(test.hasCycle(head))