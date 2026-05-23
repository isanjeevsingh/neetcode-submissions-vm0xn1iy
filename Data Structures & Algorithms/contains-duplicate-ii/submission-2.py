class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and abs(j-i) <= k:
        #             return True
        
        # return False

        H = {}
        for i, n in enumerate(nums):
            H.setdefault(n, []).append(i)
        
        for key in H:
            if len(H[key]) > 1:
                for i in range(1, len(H[key])):
                    if H[key][i] - H[key][i-1] <= k:
                        return True
        return False