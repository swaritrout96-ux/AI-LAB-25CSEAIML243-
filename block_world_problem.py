import itertools


def tsp_brute_force(distance_matrix):
  n = len(distance_matrix)
  cities = range(1, n)
  min_cost = float("inf")
  best_path = None

  for perm in itertools.permutations(cities):
    current_cost = 0
    k = 0
    for city in perm:
      current_cost += distance_matrix[k][city]
      k = city
    current_cost += distance_matrix[k][0]

    if current_cost < min_cost:
      min_cost = current_cost
      best_path = (0,) + perm + (0,)

  return best_path, min_cost