class JumpGame:
    def canJump(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return True
        longest = 0
        for i in range(len(nums) - 1):
            x = nums[i]
            longest = x if x >= longest else longest - 1
            if x == 0 and longest < 1:
                return False
        return False if longest < 1 else True

test = JumpGame()
print("Expected: True, ", test.canJump([2,3,1,1,4]))
print("Expected: False, ", test.canJump([3,2,1,0,4]))
print("Expected: True, ", test.canJump([1]))
print("Expected: True, ", test.canJump([0]))
print("Expected: False, ", test.canJump([0, 0]))
print("Expected: False, ", test.canJump([1,0,0]))
print("Expected: True, ", test.canJump([1,0]))
print("Expected: True, ", test.canJump([2,0]))
print("Expected: True, ", test.canJump([2,0,0]))
print("Expected: True, ", test.canJump([2,2]))
print("Expected: True, ", test.canJump([1,1,2,2,0,1,1]))