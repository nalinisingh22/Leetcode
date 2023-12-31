from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height)-1
        maximum = 0
        while l < r:
            area = (r-l) * (min(height[l],height[r]))
            maximum = max(maximum,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maximum

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))