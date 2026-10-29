def dfs(graph, start, goal):
  stack = [[start]]
  visited = set()

  while stack:
    path = stack.pop()
    node = path[-1]

    if node == goal:
      return path

    if node not in visited:
      visited.add(node)
      for neighbor in reversed(graph.get(node, [])):
        if neighbor not in visited:
          stack.append(path + [neighbor])
  return None