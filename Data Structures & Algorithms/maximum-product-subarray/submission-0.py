import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        max_prod = -math.inf
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                max_prod = max(max_prod,math.prod(nums[i:j]))
        return max_prod