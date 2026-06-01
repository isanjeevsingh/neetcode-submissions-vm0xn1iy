class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        res = [[1], [1,1]]
        for i in range(2, numRows):
            l = []
            last = res[-1]
            for j in range(len(last)-1):
                l.append(last[j]+last[j+1])
            l.insert(0, 1)
            l.append(1)
            res.append(l)
        return res