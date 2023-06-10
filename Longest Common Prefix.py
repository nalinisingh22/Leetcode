from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for c in strs:
                if i == len(c) or c[i] != strs[0][i] :
                    return res
            res += c[i]
        print(res)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))