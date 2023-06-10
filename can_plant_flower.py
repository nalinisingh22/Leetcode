from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == len(flowerbed)-1 or flowerbed[i+1] == 0 )and (flowerbed[i-1]==0 or i == 0):
                    count += 1
                    flowerbed[i] = 1
        print(count)
        if count >= n:
            return True
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1,0,0],2))

