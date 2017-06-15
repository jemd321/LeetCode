class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MergeTwoSortedLists:
    def merge_two_lists(self, l1, l2):
        head = current = ListNode(0)
        while l1 and l2:
            if(l1.val < l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return head.next







