from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = [-1] * len(nums1)
        # for i in range(len(nums1)):
        #     idx = nums2.index(nums1[i])
        #     for j in range(idx+1,len(nums2)):
        #         if nums2[j]>nums2[idx]:
        #             res[i] = nums2[j]
        #             break
        # return res
        # Complexity - O(m+n)
        # using Stack.
        nums1idx = {n: i for i, n in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            curr = nums2[i]

            if curr in nums1idx:
                stack.append(curr)

            while stack and stack[-1] <curr:
                val = stack.pop()
                idx = nums1idx[val]
                res[idx] = curr
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))