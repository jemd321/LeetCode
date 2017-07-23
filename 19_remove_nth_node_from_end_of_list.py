class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class RemoveNthNodeFromEndOfList:
    def removeNthFromEnd(self, head, n):
        prev_n = curr = head
        count = 0
        if not n:
            return head
        for i in range(n - 1):
            curr = curr.next
            count += 1
        # edge case: nth node is start of list
        if not curr.next and count == n - 1:
            head = prev_n.next
            return head

        curr = curr.next
        while curr.next:
            curr = curr.next
            prev_n = prev_n.next
        prev_n.next = prev_n.next.next
        return head


test = RemoveNthNodeFromEndOfList()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result_head = test.removeNthFromEnd(head, 5)

while result_head:
    print(result_head.val)
    result_head = result_head.next

