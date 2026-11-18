# algorithm.py
# AI: heuristic, minimax with alpha-beta, tree printing.

import game


def evaluate(board, ai_player):
    """Heuristic score from AI's view.
    Combines: four difference, open threes, open twos, center control.
    Returns float (high = AI winning, low = human winning)."""
    pass


def score_window(window, player):
    """Score a 4-cell window for player (4/3/2/1 pieces). Returns int."""
    pass


def count_open_threes(board, player):
    """Count windows with exactly 3 player cells + 1 EMPTY. Returns int."""
    pass


def count_open_twos(board, player):
    """Count windows with exactly 2 player cells + 2 EMPTY. Returns int."""
    pass


def center_score(board, player):
    """Sum player's pieces in center columns. Returns int."""
    pass


def make_node(board, move, depth, player):
    """Create tree node dict with keys:
    board, move, depth, value, alpha, beta, heuristic, children, pruned, player.
    Returns dict."""
    pass


def minimax(board, depth, alpha, beta, maximizing, ai_player, stats):
    """Recursive minimax with alpha-beta pruning.
    - Increments stats['nodes_expanded'].
    - Stops at depth 0 / full board: returns (evaluate(...), leaf_node).
    - Maximizer (AI) / Minimizer (human) update alpha/beta.
    - On cutoff: marks node pruned, increments stats['nodes_pruned'].
    Returns tuple (value, node)."""
    pass


def get_ai_move(board, K, ai_player):
    """Run minimax to depth K and pick best move.
    Returns dict: best_move, root, nodes_expanded, nodes_pruned, time_ms."""
    pass


def print_tree(node, indent=0):
    """Recursively print node: depth, move, value, alpha, beta, heuristic, pruned.
    Returns None."""
    pass