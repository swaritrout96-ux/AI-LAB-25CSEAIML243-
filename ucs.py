import heapq


def uniform_cost_search(graph, start, goal):
  pq = [(0, [start])]
  visited = {}

  while pq:
    cost, path = heapq.heappop(pq)
    node = path[-1]

    if node == goal:
      return path, cost

    if node in visited and visited[node] <= cost:
      continue
    visited[node] = cost

    for neighbor, weight in graph.get(node, []):
      if neighbor not in [p[0] for p in pq]:
        heapq.heappush(pq, (cost + weight, path + [neighbor]))
  return None, float("inf")