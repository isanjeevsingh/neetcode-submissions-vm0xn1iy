class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            max_freq, ch_count = 0, {}
            for j in range(i, len(s)):
                ch_count[s[j]] = ch_count.get(s[j], 0) + 1
                max_freq = max(max_freq, ch_count[s[j]])
                if (j-i+1) - max_freq <= k:
                    res = max(res, j-i+1)
        return res