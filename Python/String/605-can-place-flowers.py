class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        numberOfSpots = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0 and n < 2:
            return True
        elif len(flowerbed) == 3 and flowerbed == [0,0,0]:
            return True
        for i in range(len(flowerbed)-2):
            if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                numberOfSpots += 1
            elif i == len(flowerbed)-3 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
                numberOfSpots += 1
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                numberOfSpots += 1   
            print(numberOfSpots, i)   
        if numberOfSpots >= n:
            return True
        else:
            return False
