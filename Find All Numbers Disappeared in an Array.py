from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maximum = len(nums)
        nums = set(nums)

        res = []
        for i in range(0,maximum):
            if i+1 not in nums:
                res.append(i+1)
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([1,1]))