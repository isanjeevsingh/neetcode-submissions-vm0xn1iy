class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = min(strs)
        for i in range(len(min_word)):
            for word in strs:
                if word[i] != min_word[i]:
                    return min_word[:i]
        return min_word