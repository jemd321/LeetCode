class AddBinary:
    def add_binary(self, a, b):
        a = self.binary_decimal(a)
        b = self.binary_decimal(b)
        return self.decimal_binary(a + b)

    def binary_decimal(self, x):
        quot = 0
        for i in range(len(x)):
            quot = (quot * 2) + int(x[i])
        return quot

    def decimal_binary(self, x):
        if not x:
            return "0"
        b = ""
        while x >= 1:
            d = x % 2
            b += str(d)
            x //= 2
        return b[::-1]

class Test:
    test = AddBinary()
    print(test.add_binary("11", "1"))
    print(test.add_binary("1111", "1010"))
    print(test.add_binary("0", "0"))
    print(test.add_binary("0", "1"))


