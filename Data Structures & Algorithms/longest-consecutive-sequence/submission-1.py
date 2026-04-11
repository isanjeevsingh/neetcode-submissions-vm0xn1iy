class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_length = 1
        current = 1
        nums = sorted(list(set(nums)))
        pre = nums[0]
        for n in nums[1:]:
            if pre + 1 != n:
                max_length = max(max_length, current)
                current = 1
            else:
                current += 1
            pre = n
        
        return max(max_length, current)