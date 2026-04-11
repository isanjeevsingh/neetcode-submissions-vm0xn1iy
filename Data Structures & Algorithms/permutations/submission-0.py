class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
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

        res = [[]]
        for n in nums:
            perm_list = []
            for r in res:
                for i in range(len(r)+1):
                    perm = r.copy()
                    perm.insert(i, n)
                    perm_list.append(perm)
            res = perm_list
        return res