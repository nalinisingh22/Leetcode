#class Solution:
def lengthOfLongestSubstring(s: str) -> int:
    #abcabcbb
    l =0
    hmap=set()
    length = 0
    for r in range(len(s)):
        while s[r] in hmap:
            hmap.remove(s[l])
            l +=1
        hmap.add(s[r])
        length = max(length,len(hmap))
    print(length)
    return length
if __name__ == '__main__':

    lengthOfLongestSubstring("abcabcbb")








