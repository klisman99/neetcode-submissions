class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def exploreLand(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            exploreLand(row, col + 1)
            exploreLand(row, col - 1)
            exploreLand(row + 1, col)
            exploreLand(row - 1, col)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    exploreLand(row, col)
        
        return islands