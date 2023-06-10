from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List:
        # Brute Force : O(n*2)
        # for i in range(k):
        #     r = len(nums)-1
        #     tmp = nums[0]
        #     while r>=1:
        #         if r == len(nums)-1 :
        #             nums[0] = nums[r]
        #         else:
        #             nums[r+1],nums[r] = nums[r],nums[r+1]
        #         r -= 1
        #     nums[1] = tmp
        # print(nums)
        # return nums

        # solution 2 : use extra memory array. This is O(n)
        # res = [-1] * len(nums)
        # for i in range(len(nums)):
        #     res[(i+k)%len(nums)] = nums[i]
        # nums = res
        # return nums

        # solution 3: in place. reverse the array, then reverse the array upto k elements.
        k = k % len(nums)
        l,r = 0,len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1

        l, r = 0, k - 1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        l, r = k, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        print(nums)



if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7],3))
