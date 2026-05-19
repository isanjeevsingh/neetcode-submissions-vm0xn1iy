class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        H = {}
        max_cnt = 0
        sub_cnt = 0
        index = 0
        for i, c in enumerate(s):
            if c in H and H[c][-1] >= index:
                max_cnt = max(max_cnt, sub_cnt)
                sub_cnt = i - H[c][-1]
                index = H[c][-1]
            else:
                sub_cnt += 1

            if c in H:
                H[c].append(i)
            else:
                H[c] = [i]            


        max_cnt = max(max_cnt, sub_cnt)
        return max_cnt
