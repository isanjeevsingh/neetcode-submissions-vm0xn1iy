class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # H = {}
        # for i, n in enumerate(nums):
        #     print(f"{H.get(target-n, None)=}")
        #     if H.get(target-n, None) is not None:
        #         return [H[target-n], i]
        #     H[n] = i   
        # return -1

        H = {}
        for i, n in enumerate(nums):
            if target - n in H:
                return [H[target-n], i]
            H[n] = i