class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        hashMap = {}
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j].isdigit() and board[i][j] in hashMap:
                    elem = hashMap[board[i][j]]
                    if i in elem[0] or j in elem[1] or (i//3)*3+j//3 in elem[2]:
                        return False
                    hashMap[board[i][j]][0].add(i)
                    hashMap[board[i][j]][1].add(j)
                    hashMap[board[i][j]][2].add((i//3)*3+(j//3))
                elif board[i][j].isdigit():
                    hashMap[board[i][j]] = [{i},{j},{(i//3)*3+(j//3)}]
        return True