class RemoveElement:
    def remove_element(self, nums, val):
        n = len(nums)
        if n < 1:
            return n
        j = 0
        for i in range(n):
            curr = nums[i]
            if curr == val:
                continue
            else:
                nums[j] = curr
                j += 1
        return j

class Test:
    test = RemoveElement()
    print(test.remove_element([3, 2, 2, 3], 3))
    print(test.remove_element([3, 2, 2, 3, 4, 5, 3, 6, 7, 3, 3, 3, 4, 5], 3))
    print