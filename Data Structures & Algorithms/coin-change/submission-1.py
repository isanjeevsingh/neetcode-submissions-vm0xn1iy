class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import math

        if amount == 0:
            return 0

        H = {}

        def dfs(target):
            if target == 0:
                return 0
            
            if target not in H:
                L=[]            
                for c in coins:
                    if c <= target:
                        L.append(1 + dfs(target-c))
                H[target] = min(L) if len(L) > 0 else math.inf

            return H[target]

        cnt = dfs(amount)
        
        return -1 if cnt > amount else cnt
