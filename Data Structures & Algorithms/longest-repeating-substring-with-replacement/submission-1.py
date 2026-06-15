class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Brute force solution
        # res = 0
        # for i in range(len(s)):
        #     max_freq, ch_count = 0, {}
        #     for j in range(i, len(s)):
        #         ch_count[s[j]] = ch_count.get(s[j], 0) + 1
        #         max_freq = max(max_freq, ch_count[s[j]])
        #         if (j-i+1) - max_freq <= k:
        #             res = max(res, j-i+1)
        # return res

        ## Optimal linear time 
        l = 0
        res = 0
        cnt_map = {}
        for i in range(len(s)):
            cnt_map[s[i]] = 1 + cnt_map.get(s[i], 0)
            while (i-l+1) - max(cnt_map.values()) > k:
                cnt_map[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)
        return res