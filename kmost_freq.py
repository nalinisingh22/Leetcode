from typing import List

class Solution:
    def kmost_freq(self,nums: List[int], k: int) -> List[int]:
        solution = {}
        res = []
        for i in nums:
            solution[i] = 1 + solution.get(i,0)
        a = sorted(solution.items(), key=lambda x: x[1],reverse=True)
        for i in a:
            print(i)
        #print(k)
        for i in range(k):
            res.append(a[i][0])
        return res







if __name__ == '__main__':
    S = Solution()
    print(S.kmost_freq([1,1,1,1,2,3,2,2,3,5,5,5,6,6,6,6,6,6,6,6,6], 3))