class Solution:

    def calculate_time_taken(self, piles, k):
        time_taken = 0
        for p in piles:
            time_taken += p // k if p % k == 0 else (p // k) + 1
        return time_taken

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k =1,  max(piles)
        opt_k = 1
        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2
            time_taken = self.calculate_time_taken(piles, mid_k)
            if time_taken <= h:
                opt_k = mid_k
                max_k = mid_k-1
            else:
                min_k = mid_k+1
        return opt_k