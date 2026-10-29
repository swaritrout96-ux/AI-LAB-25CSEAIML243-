def minimax(node, depth, maximizing_player, evaluate_fn, get_children):
  if depth == 0 or not get_children(node):
    return evaluate_fn(node)

  if maximizing_player:
    max_eval = -float("inf")
    for child in get_children(node):
      eval = minimax(child, depth - 1, False, evaluate_fn, get_children)
      max_eval = max(max_eval, eval)
    return max_eval
  else:
    min_eval = float("inf")
    for child in get_children(node):
      eval = minimax(child, depth - 1, True, evaluate_fn, get_children)
      min_eval = min(min_eval, eval)
    return min_eval