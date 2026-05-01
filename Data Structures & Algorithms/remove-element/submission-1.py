class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for n in nums:
            if n != val:
                tmp.append(n)
        nums[:len(tmp)] = tmp
        # for i in range(len(tmp)):
        #     nums[i] = tmp[i]
        return len(tmp)
        