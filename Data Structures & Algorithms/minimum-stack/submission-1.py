import math
class MinStack:

    def __init__(self):
        self.min_element = None
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_element = min(self.stack)

    def pop(self) -> None:
        if len(self.stack) > 0 :
            self.stack.pop()
            if self.stack:
                self.min_element = min(self.stack)
            else:
                self.min_element = None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element
