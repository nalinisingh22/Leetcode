from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # logic - we are converting the array of int to array of str. then comparing the number by adding 2 string.
        for i,n in enumerate(nums):
            nums[i] = str(n)


        def comparison(n1,n2):
            if n1+n2 > n2+n1:
                return 1
            else:
                return -1
        nums.sort(key=cmp_to_key(comparison), reverse=True)
        ans = '0' if nums[0] == '0' else ''.join(nums)
        return ans



if __name__ == '__main__':
    s= Solution()
    print(s.largestNumber([3,30,34,5,9]))
