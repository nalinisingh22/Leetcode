class Solution:
    def valid_palindrome(self,s:str):
        t = []
        for i in range(len(s)-1,-1,-1):
            t.append(s[i])
        t = "".join(t)
        if t != s:
            return False
        else:
            return True



if __name__ == '__main__':
    S = Solution()
    print(S.valid_palindrome("amanaplanacanalpanama"))