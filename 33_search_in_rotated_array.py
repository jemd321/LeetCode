class SearchInRotatedArray:
    def search(self, nums, target):
        if not nums:
            return -1
        n = len(nums)
        if n <= 2:
            return nums.index(target) if target in nums else -1

        # Find pivot point, ie lowest value in the array using binary search.
        lower_pivot = nums[-1]
        upper_pivot = nums[0]
        if upper_pivot < lower_pivot:
            return self.binary_search(nums, target)
        if lower_pivot < target < upper_pivot:
            return -1

        low = 0
        high = len(nums) - 1
        mid = None
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid - 1] > nums[mid]:
                # Found lowest
                break
            if nums[mid] >= upper_pivot:
                # search right
                low = mid + 1
            elif nums[mid] <= lower_pivot:
                # search left
                high = mid - 1

        lowest = mid
        if target < upper_pivot:
            index = self.binary_search(nums[lowest:], target)
            return -1 if index == -1 else lowest + index
        else:
            return self.binary_search(nums[:lowest], target)

    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                # search right
                low = mid + 1
            else:
                high = mid - 1
        return -1


test = SearchInRotatedArray()
print("exp: -1", test.search([], 3))
print("exp: 0", test.search([1], 1))
print("exp: 0", test.search([1, 2], 1))
print("exp: -1", test.search([1, 2], 3))
print("exp: 2", test.search([1, 3, 5], 5))
print("exp: 3", test.search([1, 3, 5, 8], 8))
print("exp: 4", test.search([1, 3, 5, 8, 10], 10))
print("exp: 5", test.search([1, 3, 5, 8, 10, 12], 12))



print("exp: 0", test.search([4, 5, 6, 7, 0, 1, 2], 4))
print("exp: 1", test.search([4, 5, 6, 7, 0, 1, 2], 5))
print("exp: 2", test.search([4, 5, 6, 7, 0, 1, 2], 6))
print("exp: 3", test.search([4, 5, 6, 7, 0, 1, 2], 7))
print("exp: 4", test.search([4, 5, 6, 7, 0, 1, 2], 0))
print("exp: 5", test.search([4, 5, 6, 7, 0, 1, 2], 1))
print("exp: 6", test.search([4, 5, 6, 7, 0, 1, 2], 2))
print("exp: -1", test.search([4, 5, 6, 7, 0, 1, 2], -2))
print("exp: -1", test.search([4, 5, 6, 7, 0, 1, 2], 3))
print("exp: -1", test.search([4, 5, 6, 7, 0, 1, 2], 8))

print("exp: 2", test.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

print("exp: 0", test.search([4, 5, 6, 7, 8, 1, 2, 3], 4))
print("exp: 1", test.search([4, 5, 6, 7, 8, 1, 2, 3], 5))
print("exp: 2", test.search([4, 5, 6, 7, 8, 1, 2, 3], 6))
print("exp: 3", test.search([4, 5, 6, 7, 8, 1, 2, 3], 7))
print("exp: 4", test.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
print("exp: 5", test.search([4, 5, 6, 7, 8, 1, 2, 3], 1))
print("exp: 6", test.search([4, 5, 6, 7, 8, 1, 2, 3], 2))
print("exp: 7", test.search([4, 5, 6, 7, 8, 1, 2, 3], 3))

print("exp: 0", test.search([6, 7, 8, 0, 1, 2, 3, 4], 6))
print("exp: 1", test.search([6, 7, 8, 0, 1, 2, 3, 4], 7))
print("exp: 2", test.search([6, 7, 8, 0, 1, 2, 3, 4], 8))
print("exp: 3", test.search([6, 7, 8, 0, 1, 2, 3, 4], 0))
print("exp: 4", test.search([6, 7, 8, 0, 1, 2, 3, 4], 1))
print("exp: 5", test.search([6, 7, 8, 0, 1, 2, 3, 4], 2))
print("exp: 6", test.search([6, 7, 8, 0, 1, 2, 3, 4], 3))
print("exp: 7", test.search([6, 7, 8, 0, 1, 2, 3, 4], 4))
