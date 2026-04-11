class Solution:
    def isValid(self, s: str) -> bool:
        L = []
        H = {')':'(', '}':'{', ']':'['}
        for c in s:
            if len(L) > 0 and L[-1] == H.get(c,"x"):
                L.pop()
            else:
                L.append(c)
        return len(L) == 0        