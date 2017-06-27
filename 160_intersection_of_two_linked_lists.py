class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class IntersectionOfTwoLinkedLists:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        currA, currB = headA, headB
        a_len = self.list_len(headA)
        b_len = self.list_len(headB)

        while a_len > b_len:
            currA = currA.next
            a_len -= 1
        while a_len < b_len:
            currB = currB.next
            b_len -= 1

        while currA.next:
            if currA is currB:
                return currA
            currA = currA.next
            currB = currB.next

        if currA is currB:
            return currA
        return None

    @staticmethod
    def list_len(head):
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        return n


class Test:
    test = IntersectionOfTwoLinkedLists()
    headC = ListNode(4)
    headC.next = ListNode(5)
    headC.next.next = ListNode(6)

    headA = ListNode(2)
    headA.next = ListNode(3)
    headA.next.next = headC

    headB = ListNode(1)
    headB.next = ListNode(2)
    headB.next.next = ListNode(3)
    headB.next.next.next = headC

    print(test.getIntersectionNode(headA, headB).val)

    headA = ListNode(2)
    headA.next = ListNode(3)
    headA.next.next = ListNode(4)

    headB = ListNode(1)
    headB.next = ListNode(2)
    headB.next.next = ListNode(3)
    headB.next.next.next = ListNode(4)

    print(test.getIntersectionNode(headA, headB))

    headA = ListNode(1)