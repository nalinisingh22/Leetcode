from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = {0:1}  # key-value pair of (0, 1), where 0 is the sum of the empty subarray and 1 is the frequency of the empty subarray
        count = 0
        currsum = 0
        for i in nums:
            currsum += i
            d = currsum - k
            if d in res:
                count += res[d]
            if currsum in res:
                res[currsum] += 1
            else:
                res[currsum] = 1
        print(res)
        return count




if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,1,1],2))

