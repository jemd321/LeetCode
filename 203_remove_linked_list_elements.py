class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RemoveLinkedListElements:
    def removeElements(self, head, val):
        if not head:
            return None
        while head.next and head.val == val:
            head = head.next
        if not head.next and head.val == val:
            return None
        prev = curr = head
        while curr.next:
            if curr.val == val:
                prev.next = curr.next
                curr = prev
            prev = curr
            curr = curr.next
        if curr.val == val:
            curr = prev
            curr.next = None
        return head


class Test:
    test = RemoveLinkedListElements()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)


    new_head = test.removeElements(head, 6)
    while new_head.next:
        print(new_head.val)
        new_head = new_head.next
    print(new_head.val)

    h1 = ListNode(1)
    print(test.removeElements(h1, 6).val)