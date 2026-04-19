class Solution:
    H = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n-1 not in Solution.H:
            Solution.H[n-1] = self.climbStairs(n-1)

        if n-2 not in Solution.H:
            Solution.H[n-2] = self.climbStairs(n-2)

        return  Solution.H[n-1] + Solution.H[n-2]
