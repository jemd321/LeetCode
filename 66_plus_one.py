class PlusOne:
    def plus_one(self, digits):
        num = ""
        for d in digits:
            num += str(d)
        result = int(num) + 1
        result_digits = []
        for c in str(result):
            result_digits.append(int(c))
        return result_digits

class Test:
    test = PlusOne()
    print(test.plus_one([4,3,2,4,3,2,3,4,5,2]))

