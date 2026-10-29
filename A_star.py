import heapq


def a_star_search(graph, start, goal, h):
  pq = [(h(start), 0, [start])]
  visited = {}

  while pq:
    f, g, path = heapq.heappop(pq)
    node = path[-1]

    if node == goal:
      return path, g

    if node in visited and visited[node] <= g:
      continue
    visited[node] = g

    for neighbor, weight in graph.get(node, []):
      new_g = g + weight
      new_f = new_g + h(neighbor)
      heapq.heappush(pq, (new_f, new_g, path + [neighbor]))

  return None, float("inf")