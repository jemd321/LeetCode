class MoveZeroes:
    def moveZeroes(self, nums):
        n = len(nums)
        z_count = 0
        for i in range(n):
            if nums[i] == 0:
                z_count += 1
            else:
                nums[i-z_count] = nums[i]
        for j in range(n-z_count, n):
            nums[j] = 0
        return nums


class Test:
    test = MoveZeroes()
    print(test.moveZeroes([0, 1, 0, 3, 12]))
    print(test.moveZeroes([0]))
    print(test.moveZeroes([]))
    print(test.moveZeroes([1, 3, 12]))
    print(test.moveZeroes([0, 1, 0, 3, 0]))
    print(test.moveZeroes([0, 0, 0]))

