import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subbox = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] == rows[i] or board[i][j] == cols[j] or board[i][j] == subbox[i//3,j//3]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                subbox[i//3,j//3].add(board[i][j])
                return True



if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

