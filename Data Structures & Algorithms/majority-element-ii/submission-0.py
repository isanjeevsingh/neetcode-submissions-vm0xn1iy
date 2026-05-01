class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums) // 3
        H = {}
        for n in nums:
            H[n] = H.get(n, 0) + 1
        res = []
        for k in H:
            if H[k] > N:
                res.append(k)
        return res