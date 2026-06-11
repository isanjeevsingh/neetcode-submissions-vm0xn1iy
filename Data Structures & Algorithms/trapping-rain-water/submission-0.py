class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        lm, rm = 0, 0
        for i, h in enumerate(height):
            left_max[i] = lm
            lm = max(lm, h)

        for i in range(len(height)-1,-1,-1):
            right_max[i] = rm
            rm = max(rm, height[i])
        
        vol = 0
        for i, h in enumerate(height):
            t_vol = min(left_max[i], right_max[i]) - h
            if t_vol > 0:
                vol += t_vol
        
        return vol