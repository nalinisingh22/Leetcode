from typing import List

class Solution:
    def Product_Array(self,nums: List[int]) -> List[int]:
        # get the prefix and postfix for every element
        post,pre = 1,1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.Product_Array([1,2,3,4]))




