import math as mt
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [mt.prod(nums[:i]+nums[i+1:]) for i in range(len(nums))]
              