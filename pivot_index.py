from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # -----Time complexity is O(n*n)
        # for i in range(len(nums)):
        #     sum_left = 0
        #     sum_right = 0
        #     for j in range(i+1,len(nums)):
        #         sum_right += nums[j]
        #     for j in range(0,i):
        #         sum_left += nums[j]
        #     print("left---",sum_left,"right----",sum_right)
        #     if (sum_left == sum_right):
        #         print(i)
        #         break

        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


if __name__ == '__main__':
    s = Solution()
    s.pivotIndex([1,7,3,6,5,6])