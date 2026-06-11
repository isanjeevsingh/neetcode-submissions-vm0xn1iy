class Solution:
    # def two_sum(self, nums, target):
    #     H = {}
    #     for n in nums:
    #         if target - n in H:
    #             return [n, target-n]
    #         else:
    #             H[n] = 1
    #     return []


    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     H2 = {}
    #     for n in set(nums):
    #         target = -n
    #         l = self.two_sum(nums, target)
    #         if len(l) == 2:
    #             l.append(n)
    #             l.sort()
    #             key = " ".join([str(x) for x in l])
    #             H2[key] = 1
    #     K = H2.keys()
    #     L = []
    #     for k in K:
    #         L.append([int(x) for x in k.split(" ")])
    #     return L

    def two_sum(self, nums, target):
        H = {}
        res = {}
        for n in nums:
            if target - n in H:
                key = "".join([str(x) for x in sorted([n, target-n])])
                if key not in res:
                    res[key] = [n, target-n]
            H[n] = 1
        return res.values()


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = {}
        for i, n in enumerate(nums):
            trips = self.two_sum(nums[:i]+nums[i+1:], -n)
            if len(trips) > 0:
                for trip in trips:
                    key = "".join([str(x) for x in sorted(trip + [n])])
                    if key not in res:
                        res[key] = sorted(trip + [n])
        print(list(res.keys()))
        return list(res.values())

