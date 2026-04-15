class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # N = len(nums) 
        # total_sum = (N*(N+1)) // 2
        # return total_sum - sum(nums)
        
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr