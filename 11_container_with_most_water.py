class ContainerWithMostWater:
    def maxArea(self, height):
        x_left = 0
        x_right = len(height) - 1
        max_area = 0
        while x_left < x_right:
            y_left = height[x_left]
            y_right = height[x_right]
            area = (x_right - x_left) * min(y_left, y_right)
            if area > max_area:
                max_area = area
            if y_left <= y_right:
                x_left += 1
            else:
                x_right -= 1
        return max_area

test = ContainerWithMostWater()
print("Expected: 15, Actual: ", test.maxArea([2, 3, 1, 4, 3, 1, 4, 2]))
print("Expected: 7, Actual: ", test.maxArea([1, 1, 1, 1, 1, 1, 1, 1]))
print("Expected: 28, Actual: ", test.maxArea([4, 3, 1, 4, 3, 1, 4, 4]))
print("Expected: 0, Actual: ", test.maxArea([0, 0, 0, 0, 1, 0, 0, 0]))
print("Expected: 0, Actual: ", test.maxArea([0, 0, 0, 0, 0, 0, 0, 0]))





