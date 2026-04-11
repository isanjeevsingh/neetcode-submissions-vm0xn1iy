class Solution:

    def bin_search(self, A, target):
        l, r = 0, len(A)-1
        while l <= r:
            mid = (l+r) // 2
            if A[mid] < target:
                l = mid+1
            elif A[mid] > target:
                r = mid-1
            else:
                return True
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = []
        for row in matrix:
            L += row

        return self.bin_search(L, target)