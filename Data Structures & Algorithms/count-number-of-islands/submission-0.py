class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # BFS from 1s to find connected components
        visited = set()
        num_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    if (x, y) not in visited:
                        num_islands += 1
                        self.expand_from_point(grid, x, y, visited)
                        print("visited set:", visited)
        return num_islands

    
    def expand_from_point(self, grid, start_x, start_y, visited):
        print("expanding from:", start_x, start_y)
        queue = [(start_x, start_y)]
        dirs = [[1,0],[-1,0], [0,1], [0,-1]]
        is_in_bounds = lambda x,y : 0 <= x < len(grid) and 0 <= y < len(grid[0])

        while queue:
            x, y = queue.pop()
            visited.add((x, y))
            for dx, dy in dirs:
                if is_in_bounds(x + dx, y + dy) and grid[x+dx][y+dy] == '1':
                    if (x + dx, y + dy) not in visited:
                        queue.append((x + dx, y + dy))