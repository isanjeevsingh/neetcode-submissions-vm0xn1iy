class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        curr_seq = 0
        for n in nums:
            if n == 1:
                curr_seq += 1
            if n == 0:
                max_seq = max(max_seq, curr_seq)
                curr_seq = 0
        return max(curr_seq, max_seq)