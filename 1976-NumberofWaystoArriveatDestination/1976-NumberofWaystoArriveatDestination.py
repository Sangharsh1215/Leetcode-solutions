# Last updated: 3/24/2025, 2:39:55 AM
import heapq
class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        graph = {i: [] for i in range(n)}
        

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        pq = [(0, 0)]
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        
        while pq:
            time, node = heapq.heappop(pq)
            
            if time > dist[node]:
                continue
            
            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time
                
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_time, neighbor))
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1]
            
            