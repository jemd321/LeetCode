class HappyNumber:
    def isHappy(self, n):
        if not n:
            return False
        marker = n
        while n != 1:
            mid = self.calc_digits(n)
            if mid == 1:
                return True
            n = self.calc_digits(mid)
            if marker == n:
                return False
            marker = self.calc_digits(marker)
        return True


    def calc_digits(self, n):
        digits = [int(x) for x in str(n)]
        return sum(map(lambda d: d ** 2, digits))

class Test:
    test = HappyNumber()
    print(test.isHappy(19))
    print(test.isHappy(20))
    print(test.isHappy(1))