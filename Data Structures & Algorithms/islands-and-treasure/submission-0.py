class Solution:
    # Define LAND
    # Traverse each grid cell until it reaches a land
    # Use BFS to find nearest treasure
    # Find a way to control the distance
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = pow(2, 31) - 1
        WATER = -1
        TREASURE = 0
        rows, cols = len(grid), len(grid[0])

        def findTreasure(row, col):
            visited = set((row, col))
            queue = deque([(row, col, 0)])

            while queue:
                (r, c, step) = queue.popleft()

                if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == WATER or (r, c) in visited:
                    continue
                
                visited.add((r, c))

                if grid[r][c] == TREASURE:
                    grid[row][col] = step
                    return
                
                queue.append((r + 1, c, step + 1))
                queue.append((r - 1, c, step + 1))
                queue.append((r, c + 1, step + 1))
                queue.append((r, c - 1, step + 1))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND:
                    findTreasure(row, col)