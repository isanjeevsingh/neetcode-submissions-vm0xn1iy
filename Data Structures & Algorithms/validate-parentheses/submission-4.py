class Solution:
    def isValid(self, s: str) -> bool:
        # L = []
        # H = {')':'(', '}':'{', ']':'['}
        # for c in s:
        #     if len(L) > 0 and L[-1] == H.get(c,'x'):
        #         L.pop()
        #     else:
        #         L.append(c)
        # return len(L) == 0        

        S = []
        H = {')': '(', '}':'{', ']':'['}

        for b in s:
            if b in H and len(S) > 0 and S[-1] == H[b]:
                S.pop()
            else:
                S.append(b)
        
        return len(S) == 0