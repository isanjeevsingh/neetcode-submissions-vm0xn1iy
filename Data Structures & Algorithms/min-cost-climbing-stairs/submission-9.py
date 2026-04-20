class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # H = {}
        
        # def compute_cost(n):
        #     if n <= 1:
        #         return 0  # no cost to start
            
        #     if n not in H:
        #         H[n] = min(
        #             compute_cost(n-1) + cost[n-1],
        #             compute_cost(n-2) + cost[n-2]
        #         )
            
        #     return H[n]
        
        # return compute_cost(len(cost))

        H = {} 
        def compute_cost(n): 
            if n <= 1: 
                return 0 
            
            if n-1 not in H: 
                H[n-1] = cost[n-1]+compute_cost(n-1) 
            
            if n-2 not in H: 
                H[n-2] = cost[n-2]+compute_cost(n-2) 
            
            return min(H[n-1], H[n-2]) 
        
        return compute_cost(len(cost))