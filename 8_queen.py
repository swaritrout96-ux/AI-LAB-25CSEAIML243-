def solve_n_queens(n=8):
  def backtrack(row, diagonals, anti_diagonals, cols):
    if row == n:
      return [[]]
    solutions = []
    for col in range(n):
      if (
          col in cols
          or (row - col) in diagonals
          or (row + col) in anti_diagonals
      ):
        continue
      cols.add(col)
      diagonals.add(row - col)
      anti_diagonals.add(row + col)

      for sol in backtrack(row + 1, diagonals, anti_diagonals, cols):
        solutions.append([col] + sol)

      cols.remove(col)
      diagonals.remove(row - col)
      anti_diagonals.remove(row + col)
    return solutions

  return backtrack(0, set(), set(), set())