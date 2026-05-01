class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_element = nums[0]
        maj_cnt = 1
        for n in nums:
            if n == maj_element:
                maj_cnt += 1
            elif n != maj_element and maj_cnt > 0:
                maj_cnt -= 1
            elif n != maj_element and maj_cnt == 0:
                maj_element = n
                maj_cnt = 1
        
        return maj_element