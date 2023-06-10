class Solution:
    def Valid_Anagram(self,s:str,t:str):
        # Time complexity is O(nlogn)
        # if sorted(s) == sorted(t):
        #     return True
        # return False
        countS ={}
        CountT = {}
        for i in s:
            countS[i] = 1 + countS.get(i,0)
        for j in t:
            CountT[j] = 1 + CountT.get(j,0)

        #print(countS,"second",CountT)
        for i in countS:
            if countS[i] != CountT.get(i,0):
                return False
        return True




if __name__ == '__main__':
    S = Solution()
    print(S.Valid_Anagram("anagram","nagaram"))





