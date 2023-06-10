import collections
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # # hashmap and set method. left side contains set and right side has the hash map.
        # res = set()#(mid,value) hash
        # left = set()
        # rightmap = collections.Counter(s)
        # for mid in range(1,len(s)):
        #     rightmap[s[mid]] -= 1
        #     if rightmap[s[mid]] == 0:
        #         rightmap.pop(s[mid])
        #     for j in range(26):
        #         c = chr(ord('a')+j)
        #         if c in left and c in rightmap:
        #             res.add((s[mid],c))
        #     left.add(s[mid])
        # #print(res)
        # return len(res)

        # Another Method - find the unique char in left side and match if the same char exists on
        # right side and find the number of unique char.
        unique_set = set(s)
        res = 0
        for c in unique_set:
            lt = s.find(c)
            rt = s.rfind(c)
            if lt<rt:
                res += len(set(s[lt+1:rt]))
        return res





if __name__ == '__main__':
    s = Solution()
    s.countPalindromicSubsequence("bbcbaba")