from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> List:
        # bubble sort . O(n*2)
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums
        


if __name__ == '__main__':
    s = Solution()
    s.sortColors([2,0,2,1,1,0])
