class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chartoword = {}
        wordtochar = {}
        words = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i,j in zip(pattern,words):
            if i in chartoword and chartoword[i] != j:
                return False
            if j in wordtochar and wordtochar[j] != i:
                return False
            chartoword[i] = j
            wordtochar[j] = i

        return True





if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba","dog cat cat"))