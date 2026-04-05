class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                        island_size = self.get_island_size(grid, x, y)
                        if island_size > max_area:
                            max_area = island_size
        return max_area

    
    def get_island_size(self, grid, start_x, start_y):
        queue = [(start_x, start_y)]
        size = 0
        dirs = [[1,0],[-1,0], [0,1], [0,-1]]
        is_in_bounds = lambda x,y : 0 <= x < len(grid) and 0 <= y < len(grid[0])

        print("starting at", start_x, start_y)
        while queue:
            x, y = queue.pop()
            size += 1
            grid[x][y] = 0 # visit

            for dx, dy in dirs:
                if is_in_bounds(x + dx, y + dy) and grid[x + dx][y + dy] == 1:
                    print("detected neighbor island", x+dx, y+dy)
                    grid[x+dx][y+dy] = 0 # visit
                    queue.append((x + dx, y + dy))
        print("size for island starting at ", start_x, start_y , size)
        return size