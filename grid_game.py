from typing import List
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Time: O(n) Space: O(1)
        result = float("inf")
        left, right = 0, sum(grid[0])
        print(right)

        for a, b in zip(grid[0], grid[1]):
            right -= a
            result = min(result, max(left, right))
            left += b
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.gridGame([[2,5,4],[1,5,1]]))



