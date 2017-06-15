class ReverseInteger:
    def reverse(self, x):
        negative = False
        if(x < 0):
            negative = True
        rev = (str(x)[::-1])
        temp = rev.strip("-")
        result = int(temp)
        if negative:
            result *= -1
        if self.overflow_check(result):
            return 0
        return result

    def overflow_check(self, x):
        return x > 2 ** 31 or x < (-2**31) + 1



class Test:
    test = ReverseInteger()
    print(test.reverse(12345678912345456123333333333))