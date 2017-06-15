class ValidParentheses:
    def is_valid(self, s):
        stack = []
        if s == "": return False
        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            elif p == ')':
                if self.empty(stack):
                    return False
                elif stack.pop() != '(':
                    return False
            elif p == ']':
                if self.empty(stack):
                    return False
                elif stack.pop() != '[':
                    return False
            elif p == '}':
                if self.empty(stack):
                    return False
                elif stack.pop() != '{':
                    return False
        if self.empty(stack): return True
        return False

    def empty(self, stack):
        return len(stack) == 0

class Test:
    test = ValidParentheses()
    cases = ["","(",")","[","]","{","}","{}","()","[]","([)","([])","[(]","[[[[))("]
    for case in cases:
        print(case, test.is_valid(case))