class SearchInsertPosition:
    def search_insert(self, nums, target):
        if not nums:
            return 0
        high = len(nums) - 1
        low = 0
        mid = None
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if nums[mid] < target:
            return mid + 1
        else:
            return mid

class Test:
    test = SearchInsertPosition()
    print(test.search_insert([1], 3))
    print(test.search_insert([1, 2, 4, 5, 6, 7, 8, 9, 10], 3))
    print(test.search_insert([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
    print(test.search_insert([3], 3))
    print(test.search_insert([], 3))
    print(test.search_insert([1, 2], 3))
    print(test.search_insert([5], 3))
    print(test.search_insert([4, 5, 6, 7, 8, 9], 3))
    print(test.search_insert([4, 5, 6, 7, 8, 9, 10], 11))




