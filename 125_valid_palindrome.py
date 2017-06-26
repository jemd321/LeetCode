class ValidPalindrome:
    def isPalindrome(self, s):
        n = len(s)
        i = 0
        k = n -1
        while i < k:
            while i < k and not s[i].isalnum():
                i += 1
            while i < k and not s[k].isalnum():
                k -= 1
            if s[i].lower() != s[k].lower():
                return False
            i += 1
            k -= 1
        return True


class Test:
    test = ValidPalindrome()
    print(test.isPalindrome("A man, a plan, a canal: Panama"))
    print(test.isPalindrome("race a car"))