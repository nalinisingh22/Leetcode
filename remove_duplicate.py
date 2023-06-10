from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] = set(nums)
        # print(len(nums))
        # return len(nums)
        l = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[l] = nums[R]
                l += 1
        return l

if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])