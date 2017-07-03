class WordPattern:
    def wordPattern(self, pattern, str):
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False
        n = len(pattern)
        words = str.split(" ")
        if n != len(words):
            return False
        patterns = {}
        for i in range(n):
            current_pattern = pattern[i]
            if not current_pattern in patterns:
                if words[i] in patterns.values():
                    return False
                patterns[current_pattern] = words[i]
            elif patterns[current_pattern] != words[i]:
                return False
        return True


test = WordPattern()
print("Exp: True", test.wordPattern("abba", "dog cat cat dog"))
print("Exp: False", test.wordPattern("abba", "dog cat cat fish"))
print("Exp: False", test.wordPattern("aaaa", "dog cat cat dog"))
print("Exp: False", test.wordPattern("abba", "dog dog dog dog"))
print("Exp: False", test.wordPattern("a", "dog dog dog dog"))
print("Exp: False", test.wordPattern("", "dog dog dog dog"))
print("Exp: True", test.wordPattern("", ""))
print("Exp: False", test.wordPattern(" ", ""))
print("Exp: False", test.wordPattern("", " "))






