class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid = 0
        if len(flowerbed) == 1:
            return (0 if flowerbed[0] == 1 else 1) >= n
        
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    valid += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    valid += 1
                    flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 \
                    and flowerbed[i+1] == 0:
                    valid += 1
                    flowerbed[i] = 1
        print(flowerbed)
        print(f"{valid=}")
        return valid >= n