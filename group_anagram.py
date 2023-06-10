from typing import List

class Solution:
    def group_Anagram(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for word in strs:
            sortword = "".join(sorted(word))
            if sortword in solution:
                solution[sortword].append(word)
            else:
                solution[sortword] = [word]

        return solution.values()


if __name__ == '__main__':
    S = Solution()
    print(S.group_Anagram(["eat","tea","tan","ate","nat","bat"]))
