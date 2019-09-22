class Solution:
    def dfs(self,grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]!='1':
                return
        

            grid[i][j] = '0'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        if not grid:
            return number_of_islands
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    number_of_islands += 1

        
        return number_of_islands
#0(m*n) time and O(m*n) space in worst case when grid will have all '1's and dfs will iterate over the entire grid