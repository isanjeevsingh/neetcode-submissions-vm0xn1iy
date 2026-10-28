class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        H = {}
        for c in s:
            H[c] = 1 + H.get(c, 0)
        for c in t:
            if c in H:
                H[c] -= 1
            else:
                return False
        
        for k in H:
            if H[k] != 0:
                return False
        
        return True