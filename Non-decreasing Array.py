from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
            #[3 4 4]
            if i == 0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True






if __name__ == '__main__':
    s = Solution()
    print(s.checkPossibility([3,4,2,3]))