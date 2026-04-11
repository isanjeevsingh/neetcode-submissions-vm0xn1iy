class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            q = [(i, j)]
            while q:
                r, c = q.pop(0)
                adj_steps = [(1,0), (-1,0), (0, 1), (0, -1)]
                for s in adj_steps:
                    rs, cs = s[0] + r, s[1] + c
                    if rs in range(rows) and cs in range(cols) \
                        and (rs, cs) not in visited and grid[rs][cs] == "1":
                        visited.add((rs, cs))
                        q.append((rs, cs))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    bfs(i, j)
                    islands += 1
        
        return islands