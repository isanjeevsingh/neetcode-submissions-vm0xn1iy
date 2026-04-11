class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        dist = 0

        def check_fresh_fruits():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return True
            return False

        def add_land(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols \
                or grid[r][c] == 2 or grid[r][c] == 0:
                return 
            q.append((r, c))
            grid[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                add_land(r+1, c)
                add_land(r-1, c)
                add_land(r, c+1)
                add_land(r, c-1)

            if len(q) > 0:
                dist += 1
        
        return -1 if check_fresh_fruits() else dist
