class ImplementStringFind:
    # Not optimal solution:
    # O(n*m) worst case
    # Should be able to do linear time worst case
    def strStr(self, needle, haystack):
        n = len(haystack)
        m = len(needle)
        if not n and not m:
            return 0
        if m and not n:
            return -1
        if not m and n:
            return 0
        for i in range((n-m) + 1):
            if needle[0] == haystack[i]:
                if m == 1:
                    return i
                found = False
                j = 1
                for j in range(j, m):
                    if needle[j] == haystack[i + j]:
                        if j == m - 1:
                            return i
                        else:
                            continue
                    else: break
        return -1

class Test:
    test = ImplementStringFind()
    print(test.strStr("PYTHON", "ILOVEPYTHOSNAKESPYTHONSNAKES"))
    print(test.strStr("V", "ILOVEPYTHONSNAKES"))
    print(test.strStr("PYTHON", "PYTHON"))
    print(test.strStr("P", "P"))
    print(test.strStr("P", ""))
    print(test.strStr("P", "PP"))
    print(test.strStr("", "PYTHON"))
    print(test.strStr("N", "PYTHON"))
    print(test.strStr("Z", "PYTHON"))
    print(test.strStr("BOA", "PYTHON"))