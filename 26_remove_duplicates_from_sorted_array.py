class RemoveDuplicatesFromSortedArray:
    def remove_duplicates(self, nums):
        if nums is None:
            return 0
        n = len(nums)
        if n == 0:
            return n
        duplicate = False
        j = 1
        for i in range(1, n):
            curr = nums[i]
            prev = nums[i - 1]
            if curr == prev and duplicate is False:
                duplicate = True
            else:
                if curr == prev and duplicate is True:
                    continue
                else:
                    duplicate = False
                    if j < i:
                        nums[j] = curr
                    j += 1
        return j


class Test:
    test = RemoveDuplicatesFromSortedArray()
    print(test.remove_duplicates([]))
    print(test.remove_duplicates([1, 2, 3, 3, 3, 4, 5]))
    print(test.remove_duplicates([1, 2, 3, 3, 3, 4, 4, 5, 5]))
    print(test.remove_duplicates([1]))
    print(test.remove_duplicates([1, 1]))
    print(test.remove_duplicates([1, 1, 1]))
