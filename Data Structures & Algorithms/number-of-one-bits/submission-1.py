class Solution:
    def hammingWeight(self, n: int) -> int:
        # return len([x for x in bin(n).split('b')[1] if x == '1'])
        res = 0
        for i in range(0, 32):
            if (1 << i) & n:
                res += 1
        return res