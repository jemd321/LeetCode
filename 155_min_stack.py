class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        if not self.stack:
            self.min_stack.append(x)
        elif self.min_stack[-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack.append(x)

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None
        self.min_stack.pop(-1)
        return self.stack.pop(-1)

    def getMin(self):
        return self.min_stack[-1]

class Test:
    test = MinStack()
    test.push(3)
    test.push(2)
    test.push(7)
    test.push(1)

    print(test.stack)
    print(test.min_stack)
    print("Min", test.getMin())
    print("Top", test.top())
    print("Pop", test.pop())
    print("Pop", test.pop())
    print("Min", test.getMin())
    print("Top", test.top())

