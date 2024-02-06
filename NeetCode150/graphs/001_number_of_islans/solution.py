class Solution(object):
    def dfs(self, grid, i, j, m, n, visited):
        if visited[i][j] == 0 and grid[i][j] == "1":
            visited[i][j] = 1
            if i - 1 >= 0:
                self.dfs(grid, i - 1, j, m, n, visited)
            if j - 1 >= 0:
                self.dfs(grid, i, j - 1, m, n, visited)
            if i + 1 < m:
                self.dfs(grid, i + 1, j, m, n, visited)
            if j + 1 < n:
                self.dfs(grid, i, j + 1, m, n, visited)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n] * m
        l = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j, m, n, visited)