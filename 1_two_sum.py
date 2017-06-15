class TwoSum:
    def two_sum(self, nums, target):
        # Hash table with array value as key and arr index as value
        n = len(nums)
        hash_table = {}
        for i in range(n):
            if(nums[i] in hash_table):
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i


class Test:
    d = TwoSum()
    case = [3,2,4]
    test = d.two_sum(case, 6)
    for x in test:
        print(x)
