class Solution:
    def rob(self, nums: List[int]) -> int: 
        n = len(nums)
        h = {}
        def rob_amount(i):
            if i >= n:
                return 0

            if i not in h:
                h[i] = max(nums[i]+rob_amount(i+2), rob_amount(i+1))
            
            return h[i]

        return rob_amount(0)   
        