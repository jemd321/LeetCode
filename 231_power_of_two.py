class PowerOfTwo:
    def isPowerOfTwo(self, n):
        if not n:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1


class Test:
    test = PowerOfTwo()
    print(test.isPowerOfTwo(4))
    print(test.isPowerOfTwo(7))
    print(test.isPowerOfTwo(16))
    print(test.isPowerOfTwo(256))
    print(test.isPowerOfTwo(43))
    print(test.isPowerOfTwo(1))
    print(test.isPowerOfTwo(0))