class Solution(object):


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited =set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            d = [[0,1],[0,-1],[-1,0],[1,0]]
            while q:
                row, col = q.popleft()
                for dr,dc in d:
                    ri = dr+row
                    ci = dc+col
                    if (ri in range(m)) and (ci in range(n)) and grid[ri][ci]=='1' and (ri,ci) not in visited:
                        q.append((ri,ci))
                        visited.add((ri,ci))

        l = 0
        for i in range(m):
            for j in range(n):
                if not (i,j) in visited and grid[i][j] == '1':
                    bfs(i,j)
                    l+=1

        return l