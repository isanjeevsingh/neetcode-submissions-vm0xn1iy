import math as mt
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = mt.prod(nums)
        res = []
        for i, n in enumerate(nums):
            if i == 0:
                res.append(mt.prod(nums[1:]))
            else:
                res.append(mt.prod(nums[:i]+nums[i+1:]))
        return res        