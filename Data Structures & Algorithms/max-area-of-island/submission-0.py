class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        max_area = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            area = 0
            q = [(i, j)]
            while q:
                area += 1
                r, c = q.pop(0)
                adj_steps = [(1,0), (-1,0), (0, 1), (0, -1)]
                for s in adj_steps:
                    rs, cs = s[0] + r, s[1] + c
                    if rs in range(rows) and cs in range(cols) \
                        and (rs, cs) not in visited and grid[rs][cs] == 1:
                        visited.add((rs, cs))
                        q.append((rs, cs))
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    area = bfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area