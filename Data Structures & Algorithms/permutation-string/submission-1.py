class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = sorted(s1)

        def check_same(s2):
            return s1 == sorted(s2)

        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        for i in range(len(s2)):
            if check_same(s2[i:i+n]):
                return True
        
        return False
        