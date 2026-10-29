class TicTacToe:

  def __init__(self):
    self.board = [" "] * 9

  def check_winner(self, board):
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in wins:
      if board[a] == board[b] == board[c] and board[a] != " ":
        return board[a]
    if " " not in board:
      return "Tie"
    return None