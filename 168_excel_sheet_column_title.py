class ExcelSheetColumnTitle:
    def convertToTitle(self, n):
        if not n:
            return None
        result = ""
        while n > 26:
            d = n % 26
            if d == 0:
                d = 26
                n = (n // 26) - 1
            else:
                n //= 26
            result = chr(64 + d) + result

        return chr(64 + n) + result

class Test:
    test = ExcelSheetColumnTitle()
    print(test.convertToTitle(27))