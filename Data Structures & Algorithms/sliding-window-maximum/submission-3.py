from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = [max(nums[:k])]
        # max_num = res[0]
        # i = 1
        
        # while i + k <= len(nums):
        #     if nums[i-1] == max_num:
        #         max_num = max(nums[i:i+k])
        #         res.append(max_num)
        #     else:
        #         # print(f"{i=} {max_num=} {nums[i+k-1]=}")
        #         max_num = max(max_num, nums[i+k-1])
        #         res.append(max_num) 
        #     i += 1
        # return res

        res = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r+1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res









