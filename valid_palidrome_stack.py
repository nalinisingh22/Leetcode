class Solution:
    def stack_palindrome(self,s:str):
        # implementing stack solution:
        # stack = []
        # for c in s:
        #     stack.append(c)
        # for c in s:
        #     if c != stack.pop():
        #         return False
        # return True

        # implementing Queue Solution:
        right = len(s)-1
        left = 0
        while left<right:
            if s[right] != s[left]:
                return False
            left += 1
            right -= 1
        return True



if __name__ == '__main__':
    S = Solution()
    print(S.stack_palindrome("amanaplanacanalpanam"))