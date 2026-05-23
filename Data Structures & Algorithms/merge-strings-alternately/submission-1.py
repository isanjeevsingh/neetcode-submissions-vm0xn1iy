class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag1, flag2 = False, False
        if len(word1) >= len(word2):
            flag1 = True
        else:
            flag2 = True

        min_length = min(len(word1), len(word2))

        res = ""
        for i in range(min_length):
            res += word1[i] + word2[i]
        
        if flag1:
            res += word1[min_length:]
        else:
            res += word2[min_length:]

        return res