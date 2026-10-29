from collections import deque


def water_jug_bfs(cap1, cap2, target):
  queue = deque([((0, 0), [])])
  visited = {(0, 0)}

  while queue:
    (j1, j2), path = queue.popleft()

    if j1 == target or j2 == target:
      return path + [(j1, j2)]

    states = [
        (cap1, j2),
        (j1, cap2),
        (0, j2),
        (j1, 0),
        (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
        (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1)),
    ]

    for state in states:
      if state not in visited:
        visited.add(state)
        queue.append((state, path + [(j1, j2)]))
  return None