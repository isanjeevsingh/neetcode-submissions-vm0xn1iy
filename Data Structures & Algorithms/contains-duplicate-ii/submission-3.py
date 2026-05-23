class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # H = {}
        # for i, n in enumerate(nums):
        #     H.setdefault(n, []).append(i)
        
        # for key in H:
        #     if len(H[key]) > 1:
        #         for i in range(1, len(H[key])):
        #             if H[key][i] - H[key][i-1] <= k:
        #                 return True
        # return False

        window = set()

        for r in range(len(nums)):
            if nums[r] in window:
                return True
            
            window.add(nums[r])

            if len(window) > k:
                window.remove(nums[r-k])
        
        return False