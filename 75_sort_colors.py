class SortColors:
    # red = 0
    # white = 1
    # blue = 2

    def sortColors(self, nums):
        red_count = 0
        white_count = 0
        blue_count = 0
        for i in range(len(nums)):
            color = nums[i]
            if color == 0:
                red_count += 1
            elif color == 1:
                white_count += 1
        for i in range(red_count):
            nums[i] = 0
        for i in range(red_count, (red_count + white_count)):
            nums[i] = 1
        for i in range((red_count + white_count), len(nums)):
            nums[i] = 2
        return nums


test_sort = SortColors()
test_colors = [1, 0, 1, 2, 0, 2, 2, 1, 0, 2]
print(test_sort.sortColors(test_colors))
print(test_sort.sortColors([]))
print(test_sort.sortColors([0]))
print(test_sort.sortColors([1]))
print(test_sort.sortColors([2]))
print(test_sort.sortColors([0,0,0]))
print(test_sort.sortColors([1,1,1]))
print(test_sort.sortColors([2,2,2]))

