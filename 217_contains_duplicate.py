class ContainsDuplicate:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


class Test:
    test = ContainsDuplicate()
    print(test.containsDuplicate([1,2,3,4,5]))
    print(test.containsDuplicate([1,2,3,4,5,5]))