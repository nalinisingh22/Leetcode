import collections
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for i in numset:
            if i-1 not in numset:
                count=0
                while count+i in numset:
                    count += 1
                    res = max(res,count)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))







if __name__ == '__main__':
    s = Solution()
    s.longestConsecutive([100,4,200,1,3,2])
