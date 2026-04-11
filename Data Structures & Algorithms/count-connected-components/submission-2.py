class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = [False]*n
        cc_count = 0
        
        def dfs(i):
            s = deque([i])
            while s:
                print(f"{s=}")
                v = s.pop()
                visited[v] = True
                for u in adj[v]:
                    if not visited[u]:
                        s.append(u)

        for i in range(n):
            #print(visited)
            if not visited[i]:
                dfs(i)
                cc_count += 1

        return cc_count
