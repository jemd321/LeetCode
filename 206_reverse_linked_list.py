class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReverseLinkedList:
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        prev = curr = head
        curr = curr.next
        prev.next = None
        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev
        head = curr
        return head

class Test:
    test = ReverseLinkedList()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)

    new_head = test.reverseList(head)
    while new_head.next:
        print(new_head.val)
        new_head = new_head.next
    print(new_head.val)

