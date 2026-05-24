class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(n-x) for n in arr]
        H = {}
        for i in range(len(diff)-k+1):
            if sum(diff[i:i+k]) not in H:
                H[sum(diff[i:i+k])] = (i, i+k)

        return arr[H[min(H.keys())][0] : H[min(H.keys())][1]]