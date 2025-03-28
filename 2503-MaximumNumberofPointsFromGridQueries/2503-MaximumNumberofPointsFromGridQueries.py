# Last updated: 3/29/2025, 3:21:08 AM
import heapq

class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        k = len(queries)
    
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        answer = [0] * k

        min_heap = [(grid[0][0], 0, 0)]  
        visited = set([(0, 0)])
        points = 0  
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for idx, query in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                value, r, c = heapq.heappop(min_heap)
                points += 1  
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))

            answer[idx] = points
        
        return answer
