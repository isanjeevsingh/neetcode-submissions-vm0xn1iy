class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [x for x in range(n)]
        rank = [1]*n
        comp = n

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]


        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return True
            
            nonlocal comp
            comp -= 1
            if rank[r1] >= rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[r1]
            
            return False
        
        for edge in edges:
            if union(edge[0], edge[1]):
                return False

        # print(f"{parent=}")
        # print(f"{rank=}")

        return comp == 1        