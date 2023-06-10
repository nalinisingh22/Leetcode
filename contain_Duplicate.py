class Solution:
    def containsDuplicate(self, nums) -> bool:
        #set Method Solution
        h = set()
        for i in nums:
            if i in h:
                return True
            h.add(i)
        return False

if __name__ == '__main__':
    S = Solution()
    print(S.containsDuplicate([1,2,3,1]))

