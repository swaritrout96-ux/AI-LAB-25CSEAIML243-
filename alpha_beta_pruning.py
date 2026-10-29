def alpha_beta(
    node, depth, alpha, beta, maximizing_player, evaluate_fn, get_children
):
  if depth == 0 or not get_children(node):
    return evaluate_fn(node)

  if maximizing_player:
    max_eval = -float("inf")
    for child in get_children(node):
      eval = alpha_beta(
          child, depth - 1, alpha, beta, False, evaluate_fn, get_children
      )
      max_eval = max(max_eval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
        break
    return max_eval
  else:
    min_eval = float("inf")
    for child in get_children(node):
      eval = alpha_beta(
          child, depth - 1, alpha, beta, True, evaluate_fn, get_children
      )
      min_eval = min(min_eval, eval)
      beta = min(beta, eval)
      if beta <= alpha:
        break
    return min_eval