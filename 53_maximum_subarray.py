class MaximumSubArray:
    def max_sub_array(self, nums):
        n = len(nums)
        mx = -2**31 + 1
        total = 0
        for i in range(n):
            if total < 0:
                total = nums[i]
            else:
                total += nums[i]
            if(total > mx):
                mx = total
        return mx


class Test:
    test = MaximumSubArray()
    print(test.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    print(test.max_sub_array([]))
    print(test.max_sub_array([0]))
    print(test.max_sub_array([-1]))
    print(test.max_sub_array([-1, -2]))




















