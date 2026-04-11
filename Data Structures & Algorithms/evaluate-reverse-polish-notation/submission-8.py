class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for t in tokens:
            print(f"stack: {stack}")
            if t in "+-*/":
                t2, t1 = stack.pop(), stack.pop()
            if t == "+":
                stack.append(t1 + t2)
            elif t == "*":
                stack.append(t1 * t2)
            elif t == "-":
                stack.append(t1 - t2)
            elif t == "/":
                stack.append(int(t1 / t2))
            else:
                stack.append(int(t))
        return stack[0]
                
                