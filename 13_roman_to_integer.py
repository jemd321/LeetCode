class RomanToInteger:

    #input string,m output int
    # Input range 1 -3999

    def roman_to_integer(self, s):
        numerals = {"I":1,"V":5,"X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        double_numeral = False
        for i, c in enumerate(s):
            if double_numeral is True:
                double_numeral = False
                continue
            if i == len(s) - 1:
                sum += numerals[c]
            else:
                following = s[i + 1]
                if c == 'I' and following == 'V':
                    sum += 4
                    double_numeral = True
                elif c == 'I' and following == 'X':
                    sum += 9
                    double_numeral = True
                elif c == 'X' and following == 'L':
                    sum += 40
                    double_numeral = True
                elif c == 'X' and following == 'C':
                    sum += 90
                    double_numeral = True
                elif c == 'C' and following == 'D':
                    sum += 400
                    double_numeral = True
                elif c == 'C' and following == 'M':
                    sum += 900
                    double_numeral = True
                else:
                    sum += numerals[c]
        return sum

class Test:
    test = RomanToInteger()
    print(test.roman_to_integer("MMXXVII"))
    print(test.roman_to_integer("MCDXLIX"))
    print(test.roman_to_integer("DCXXII"))

