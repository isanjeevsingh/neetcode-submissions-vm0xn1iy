class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if grid is None:
            return 0

        rows, cols = len(grid), len(grid[0])
        adj_steps = [(1,0), (-1,0), (0, 1), (0, -1)] 
        INF = 2147483647
        
        def bfs(i, j):
            q = deque([(i, j)])   
            visit = [[False] * cols for _ in range(rows)]
            visit[i][j] = True                    
            dist = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return dist
                    
                    for s in adj_steps:
                        rs, cs = s[0] + r, s[1] + c                                            
                        if rs in range(rows) and cs in range(cols) \
                            and not visit[rs][cs] and grid[rs][cs] != -1:
                            q.append((rs, cs))
                            visit[rs][cs] = True
                dist += 1
            return INF


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)
        