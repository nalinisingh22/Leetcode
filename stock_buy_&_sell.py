from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    def btbuy(self,prices: List[int])-> int:
        l,r = 0, 1
        maxprofit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                currprice = prices[r] - prices[l]
                maxprofit = max(currprice, maxprofit)
            r += 1
        return maxprofit



if __name__ == '__main__':
    s = Solution()
    #s.maxProfit([7,1,5,3,6,4])
    print(s.btbuy([7,5,1,3,6,4]))
