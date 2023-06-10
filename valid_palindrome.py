class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if ord(i) >= 97 and ord(i) <=122:
                res +=i
            elif ord(i) >= 65 and ord(i) <=90:
                i = ord(i) + 32
                res += chr(i)
            elif ord(i) >= ord('0') and ord(i)<= ord('9'):
                res += i

            else:
                continue
        print(res)
        l , r = 0 , len(res)-1
        while l<r:
            if res[l] != res[r]:
                return False
            l+= 1
            r-=1
        return True





if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("0P"))