from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        boats = 0
        while l <= r:
            remaining = limit - people[r]
            boats += 1
            r -= 1
            if remaining >= people[l]:
                l+=1
        return boats



if __name__ == '__main__':
    s = Solution()
    s.numRescueBoats([3,2,2,1],3)