class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 for x in details if int(x[len(x)-4:len(x)-2]) > 60])
        