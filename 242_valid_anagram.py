class ValidAnagram():
    def isAnagram(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        s_ordered = self.sort_string(s)
        t_ordered = self.sort_string(t)

        for i in range(len(s)):
            if s_ordered[i] != t_ordered[i]:
                return False
        return True

    def sort_string(self, s):
        unicodes = [ord(c) for c in s]
        unicodes.sort()
        return unicodes

class Test:
    test = ValidAnagram()
    print(test.isAnagram("tenetenba", "benaetnet"))