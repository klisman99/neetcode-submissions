class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def countArea(row, col):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or grid[row][col] == 0
            ):
                return 0
            grid[row][col] = 0
            count = 1

            count += countArea(row + 1, col)
            count += countArea(row - 1, col)
            count += countArea(row, col + 1)
            count += countArea(row, col - 1)

            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, countArea(row, col))
        
        return max_area
