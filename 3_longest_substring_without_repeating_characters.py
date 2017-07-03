class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s):
        distinct_chars = {}
        max_substring = 0
        j = 0
        for i in range(len(s)):
            c = s[i]
            if c in distinct_chars.keys():
                j = max(distinct_chars[c], j)
            max_substring = max(max_substring, (i-j) + 1)
            distinct_chars[c] = i + 1
        return max_substring

test = LongestSubstringWithoutRepeatingCharacters()

print("Exp: 3", test.lengthOfLongestSubstring("abcabcbb"))
print("Exp: 1", test.lengthOfLongestSubstring("bbbbb"))
print("Exp: 3", test.lengthOfLongestSubstring("pwwkew"))
print("Exp: 3", test.lengthOfLongestSubstring("dvdf"))

print("Exp: 0", test.lengthOfLongestSubstring(""))
print("Exp: 1", test.lengthOfLongestSubstring("a"))
print("Exp: 2", test.lengthOfLongestSubstring("ab"))



