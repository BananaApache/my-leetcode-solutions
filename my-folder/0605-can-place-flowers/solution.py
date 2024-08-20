class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        good_spots = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False

        for index in range(len(flowerbed)):
            # front
            if index == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                good_spots += 1
                flowerbed[index] = 1
                print("front")
            # end
            elif index == len(flowerbed) - 1 and flowerbed[index - 1] == 0 and flowerbed[index] == 0:
                good_spots += 1
                flowerbed[index] = 1
                print("end")
            # middle
            elif index != 0 and index != len(flowerbed) - 1:
                if flowerbed[index - 1] == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    good_spots += 1
                    flowerbed[index] = 1
                    print("middle")
        
        print(good_spots)
        return good_spots >= n

