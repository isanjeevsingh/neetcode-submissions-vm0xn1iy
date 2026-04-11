class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        N = len(temperatures)
        for i in range(N-1):
            warm_day = 0
            warm_flag = False
            for j in range(i+1, N):
                if temperatures[j] > temperatures[i]:
                    warm_flag = True
                    break
                else:
                    warm_day += 1
            if warm_flag:
                output.append(warm_day + 1)
            else:
                output.append(0)
        output.append(0)
        return output