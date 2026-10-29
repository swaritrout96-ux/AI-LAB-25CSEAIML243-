def hill_climbing(problem_state, get_neighbors, get_value):
  current = problem_state
  current_val = get_value(current)

  while True:
    neighbors = get_neighbors(current)
    if not neighbors:
      break

    best_neighbor = max(neighbors, key=get_value)
    best_val = get_value(best_neighbor)

    if best_val <= current_val:
      break

    current, current_val = best_neighbor, best_val

  return current, current_val