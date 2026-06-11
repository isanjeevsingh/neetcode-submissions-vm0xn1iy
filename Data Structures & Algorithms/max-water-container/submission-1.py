class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # max_vol = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         vol = (j-i)*min(heights[j], heights[i])
        #         max_vol = max(max_vol, vol)
        # return max_vol

        i, j = 0, len(heights)-1
        max_vol = 0
        while i < j:
            vol = (j-i)*min(heights[j], heights[i])
            max_vol = max(max_vol, vol)
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return max_vol