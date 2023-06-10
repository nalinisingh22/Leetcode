from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        currsum = 0
        res = {0:-1}
        for i,n in enumerate(nums):
            currsum += n
            if currsum % k not in res:
                res[currsum % k] = i
            elif i - res[currsum % k] >1:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.checkSubarraySum([23,2,4,6,7],10)
