class LongestCommonPrefix:

    def longest_common_prefix(self, strs):
        # Find Shortest string in array to avoid out of range indexing
        # Compare each char in the shortest to it's equivalent position
        # As soon as there is mis match, previous index = solution
        # Should be O(n**2)
        n = len(strs)
        if n < 1: return ""
        if n == 1: return strs[0]
        strs.sort()
        shortest = strs[0]
        for i, c in enumerate(shortest):
            for j in range(1, n):
                if c != strs[j][i]:
                    if i == 0: return ""
                    return shortest[:i]
        if len(shortest) >= 1: return shortest
        return ""

class Test:
    test = LongestCommonPrefix()
    print(test.longest_common_prefix(["a","b"]))
    print(test.longest_common_prefix(["c","c"]))
    print(test.longest_common_prefix(["aa","aa"]))
    print(test.longest_common_prefix(["prefixed","predict","prenatal","prevent","preamble","preach"]))
