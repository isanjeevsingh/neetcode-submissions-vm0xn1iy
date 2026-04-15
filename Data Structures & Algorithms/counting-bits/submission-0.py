class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one(n):
            res = 0
            for i in range(0, 32):
                if (1 << i) & n:
                    res += 1
            return res

        R = []
        for i in range(n+1):
            R.append(count_one(i))
        return R
        