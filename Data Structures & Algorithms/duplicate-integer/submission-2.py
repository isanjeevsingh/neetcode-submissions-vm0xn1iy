class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # H = {}
        # for n in nums:
        #     if H.get(n, 0) > 0:
        #         return True
        #     else:
        #         H[n] = 1
        # return False

        return len(set(nums)) != len(nums)