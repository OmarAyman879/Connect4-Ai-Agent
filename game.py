# game.py
# Pure game logic

EMPTY = 0
HUMAN = 1
AI = 2
ROWS = 6
COLS = 7


def create_board(rows=ROWS, cols=COLS):
    """Create empty board. Returns 2D list filled with EMPTY."""
    pass


def copy_board(board):
    """Deep copy board. Returns new 2D list."""
    pass


def valid_moves(board):
    """Return list of columns with an empty top cell."""
    pass


def drop_piece(board, col, player):
    """Drop piece in lowest empty row of col. Returns new board or None if invalid."""
    pass


def is_full(board):
    """Check if no valid moves remain. Returns bool."""
    pass


def count_connected_fours(board, player):
    """Count 4-in-a-row (horizontal, vertical, both diagonals) for player. Returns int."""
    pass