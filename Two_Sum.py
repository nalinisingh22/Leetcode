class Solution:
    def Two_Sum(self,nums,target):
        hmap = {}
        for i,j in enumerate(nums):
            if target-j in hmap:
                return [i,hmap[target-j]]
            hmap[j] = i

if __name__ == '__main__':
    s = Solution()
    print(s.Two_Sum([2,7,11,15],9))