class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = {}
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j,h):
            if ((i,j) in visited and visited[(i,j)]>h) or (i,j) not in visited:
                visited[(i,j)] = h
                if i+1<m and grid[i+1][j]==1:
                    dfs(i+1,j,h+1)
                if j+1<n and grid[i][j+1]==1:
                    dfs(i,j+1,h+1)
                if i-1>=0 and grid[i-1][j]==1:
                    dfs(i-1,j,h+1)
                if j-1>=0 and grid[i][j-1]==1:
                    dfs(i,j-1,h+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    dfs(i,j,0)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    return -1
        return max(visited.values()) if visited else 0