class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.and_value = [-1] * n  

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y, weight):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.and_value[root_x] &= self.and_value[root_y] & weight
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.and_value[root_y] &= self.and_value[root_x] & weight
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
                self.and_value[root_x] &= self.and_value[root_y] & weight
        else:
            self.and_value[root_x] &= weight

class Solution(object):
    def minimumCost(self, n, edges, queries):
        dsu = DSU(n)

        for u, v, w in edges:
            dsu.union(u, v, w)

        result = []
        for si, ti in queries:
            if dsu.find(si) != dsu.find(ti):
                result.append(-1)
            else:
                result.append(dsu.and_value[dsu.find(si)])

        return result


            