class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        S = [[]]
        for n in nums:
            S += [s + [n] for s in S]
            print(f"{S=}")
        return S