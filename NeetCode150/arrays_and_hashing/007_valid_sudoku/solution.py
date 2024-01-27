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
                    if i in hashMap[board[i][j]][0] or j in hashMap[board[i][j]][1]:
                        return False
                    hashMap[board[i][j]][0].add(i)
                    hashMap[board[i][j]][1].add(j)
                elif board[i][j].isdigit():
                    hashMap[board[i][j]] = [{i},{j}]
        print(hashMap)
        return True