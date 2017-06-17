class ClimbingStairs:
    def climb_stairs(self, n):
        if n <= 2:
            return n
        x = 1
        y = 2
        z = 0
        for i in range(2, n):
            z = x + y
            x, y = y, z
        return z

class Test:
    test = ClimbingStairs()
    for i in range(20):
        print(test.climb_stairs(i))