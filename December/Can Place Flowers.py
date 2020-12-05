class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        def consecutive(flowerbed, n):
            count = 0
            for i in range(0, len(flowerbed)):
                if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] != 1) and (
                        i == len(flowerbed) - 1 or flowerbed[i + 1] != 1):
                    flowerbed[i] = 1
                    count += 1
            if count >= n:
                return True
            return False

        return consecutive(flowerbed, n)
