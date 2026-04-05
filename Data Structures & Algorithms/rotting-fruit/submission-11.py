class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        num_fresh_fruits = 0
        queue = []

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    num_fresh_fruits += 1
                if grid[x][y] == 2:
                    queue.append((x,y,0))
        
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        is_valid = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        time_elapsed = 0
        while queue:
            x,y,t = queue.pop(0)
            if t > time_elapsed:
                time_elapsed = t

            for dx, dy in dirs:
                if is_valid(x + dx , y + dy):
                    if grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 2
                        num_fresh_fruits -= 1
                        queue.append((x+dx, y+dy, t+1))       
        return time_elapsed if num_fresh_fruits == 0 else -1
