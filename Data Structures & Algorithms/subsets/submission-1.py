class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Iterative Solution
        # S = [[]]
        # for n in nums:
        #     S += [s + [n] for s in S]
        #     print(f"{S=}")
        # return S

        R = []
        S = []

        def dfs(i):
            if i >= len(nums):
                R.append(S.copy())
                return 

            S.append(nums[i])
            dfs(i+1)

            S.pop()
            dfs(i+1)

        dfs(0)

        return R        