class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    self.expand_from_treasure_chest(grid, x, y)
        
    

    def expand_from_treasure_chest(self, grid, start_x, start_y):
        queue = [(start_x, start_y, 0)]
        visited = set()
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        in_bounds = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])

        while queue:
            x, y, dist = queue.pop(0)
            visited.add((x, y))
            for dx, dy in dirs:
                if in_bounds(x + dx , y + dy):
                    if grid[x + dx][y + dy] != -1:
                        # update if shorter
                        if dist + 1 < grid[x + dx][y + dy]:
                            grid[x + dx][y + dy] = dist + 1
                            if (x + dx, y + dy) not in visited:
                                queue.append((x + dx, y + dy, dist + 1))
        