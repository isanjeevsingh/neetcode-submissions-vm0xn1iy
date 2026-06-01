class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            tmp = arr[i]
            arr[i] = max_num
            max_num = max(max_num, tmp)
        return arr