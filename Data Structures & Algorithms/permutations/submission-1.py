class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1. Recursion
        # if len(nums) == 0:
        #     return [[]]

        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res

        # 2. Iteration
        # res = [[]]
        # for n in nums:
        #     perm_list = []
        #     for r in res:
        #         for i in range(len(r)+1):
        #             perm = r.copy()
        #             perm.insert(i, n)
        #             perm_list.append(perm)
        #     res = perm_list
        # return res

        # 3. Backtracking
        
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False