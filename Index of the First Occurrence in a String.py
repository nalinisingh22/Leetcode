class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        # return haystack.find(needle)
        # Another Method:Pointer
        # sliding windows concept :
        i = 0
        j = len(needle)
        while j <= len(haystack):
            currneedle = haystack[i:j]
            print(currneedle)
            if currneedle == needle:
                return i
            i += 1
            j += 1
        return -1





if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello","ll"))
