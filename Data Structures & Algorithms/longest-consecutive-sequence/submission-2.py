class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        num_set = set(nums)
        seq_list = []
        max_seq = 1
        for n in list(num_set):
            if n-1 not in num_set:
                seq_counter = 1
                while n+1 in num_set:
                    seq_counter += 1
                    n = n+1
                max_seq = max(max_seq, seq_counter)
        return max_seq
