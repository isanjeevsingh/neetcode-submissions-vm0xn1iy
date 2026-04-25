class Solution:
    def rob(self, nums: List[int]) -> int:        
        n =len(nums)
        if n <= 2:
            return max(nums)

        def loot(i, arr):
            if i >= n-1:
                return 0
            
            if i not in h:
                h[i] = max(arr[i]+loot(i+2, arr), loot(i+1, arr))
            return h[i]
        
        h = {}
        val1 = loot(0, nums[1:])
        h = {}
        val2 = loot(0, nums[:n-1])
        
        return max(val1, val2)