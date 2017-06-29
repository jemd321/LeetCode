class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class PalindromeLinkedList:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.nexta
        curr = head
        n = len(stack)
        while curr and len(stack) > n // 2:
            if curr.val != stack.pop(-1):
                return False
            curr = curr.next
        return True


class Test:
    test = PalindromeLinkedList()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(1)

    print(test.isPalindrome(head))