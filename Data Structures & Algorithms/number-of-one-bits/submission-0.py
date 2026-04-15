class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([x for x in bin(n).split('b')[1] if x == '1'])