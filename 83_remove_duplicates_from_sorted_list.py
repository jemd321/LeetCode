class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveDuplicatesFromSortedList:
    def remove_duplicates(self, head):
        if not head:
            return None
        current = head
        while current.next:
            if current.next.val == current.val:
                dup = current
                while dup.next != None:
                    if dup.next.val == dup.val:
                        dup = dup.next
                current.next = dup.next
            else:
                current = current.next
        return head

class Test:
    test = RemoveDuplicatesFromSortedList()
    testList = ListNode(0)
    x = testList
    for i in range(1, 10):
        x.next = ListNode(5)
        #if i > 2 and i < 6:
        #    x.val = 3
        x = x.next

    current = test.remove_duplicates(testList)
    while current.next != None:
        print(current.val)
        current = current.next
    print(current.val)