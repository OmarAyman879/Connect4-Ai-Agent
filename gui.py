# gui.py
# PySide6 GUI: board widget, AI worker thread, main window.

import sys
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow,
    QVBoxLayout, QHBoxLayout, QLabel,
    QTreeWidget, QTreeWidgetItem, QPushButton,
)

import game
import algorithm

CELL = 70   # pixel size of one cell
K = 4       # minimax search depth


class BoardWidget(QWidget):
    """Draws the board and emits column_clicked(col) on click."""

    column_clicked = Signal(int)

    def __init__(self):
        """Init empty board and fixed widget size. Returns None."""
        pass

    def update_board(self, board):
        """Store new board and repaint. Returns None."""
        pass

    def paintEvent(self, event):
        """Draw board cells and discs. Returns None."""
        pass

    def mousePressEvent(self, event):
        """Emit column_clicked based on click x-coordinate. Returns None."""
        pass


class AIWorker(QThread):
    """Runs minimax in a background thread and emits finished(result)."""

    finished = Signal(dict)

    def __init__(self, board, depth, ai_player):
        """Store search parameters. Returns None."""
        pass

    def run(self):
        """Call algorithm.get_ai_move and emit result dict. Returns None."""
        pass


class MainWindow(QMainWindow):
    """Hosts board widget, status label, reset button, and tree view."""

    def __init__(self):
        """Build UI and initialize game state. Returns None."""
        pass

    def on_human_move(self, col):
        """Apply human move, then start AI or end game. Returns None."""
        pass

    def run_ai(self):
        """Start AIWorker for the current board. Returns None."""
        pass

    def on_ai_done(self, result):
        """Apply AI move, update tree and status, re-enable human. Returns None."""
        pass

    def check_game_over(self):
        """End game if board full; show scores. Returns bool."""
        pass

    def update_tree(self, node):
        """Rebuild QTreeWidget from root node. Returns None."""
        pass

    def make_item(self, node):
        """Recursively build QTreeWidgetItem from node dict. Returns QTreeWidgetItem."""
        pass

    def reset_game(self):
        """Reset board, flags, and widgets for a new game. Returns None."""
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())