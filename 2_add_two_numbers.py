class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers:
    def addTwoNumbers(self, l1, l2):
        result = self.sum_linked_list(l1) + self.sum_linked_list(l2)
        digits = [int(x) for x in str(result)]
        digits = digits[::-1]
        result_list = curr = ListNode(digits[0])
        for i in range(1, len(digits)):
            curr.next = ListNode(digits[i])
            curr = curr.next
        return result_list

    def sum_linked_list(self, l):
        digits = ""
        while l:
            digits += str(l.val)
            l = l.next
        return int(digits[::-1])


test = AddTwoNumbers()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = test.addTwoNumbers(l1, l2)

print("Exp: 708")
while result:
    print(result.val)
    result = result.next