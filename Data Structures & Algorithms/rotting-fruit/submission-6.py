class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        min_time = 0
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
        print("initial q", queue)
        while queue and num_fresh_fruits > 0:
            x,y,t = queue.pop(0)
            print("popped", x , y, grid[x][y], t)
            if t > time_elapsed:
                time_elapsed = t

            for dx, dy in dirs:
                if is_valid(x + dx , y + dy):
                    if grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 2
                        num_fresh_fruits -= 1
                        print("appending", x + dx, y + dy, t + 1)
                        queue.append((x+dx, y+dy, t+1))
        for _,_,t in queue:
            if t > time_elapsed:
                time_elapsed = t        
        return time_elapsed if num_fresh_fruits == 0 else -1
