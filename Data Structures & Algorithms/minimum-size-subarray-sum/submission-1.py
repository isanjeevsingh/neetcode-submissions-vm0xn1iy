class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # min_sol = float('inf')
        # print(f"{nums}")
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)+1):
        #         # print(f"{nums[i:j]=}")
        #         if sum(nums[i:j]) >= target:
        #             min_sol = min(min_sol, len(nums[i:j]))
        # return min_sol if min_sol != float('inf') else 0

        res = len(nums) + 1
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
        
        return res if res != len(nums) + 1 else 0
