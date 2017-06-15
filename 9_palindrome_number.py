class PalindromeNumber:

    # My O(n) solution, with extra space required
    def is_palindrome(self, x):
        if x < 0: return False
        digits = [i for i in str(x)]

        n = len(digits)
        k = n -1
        for i in range(n // 2):
            if digits[i] != digits[k]:
                return False
            k -= 1
        return True

class Test:
    test = PalindromeNumber()
    print(test.is_palindrome(1231))