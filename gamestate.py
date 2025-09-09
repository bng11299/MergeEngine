# gamestate.py
from unit import Unit

class GameState:
    def __init__(self, board=None, bench=None, elixir=0, shop=None):
        self.board = board if board else []
        self.bench = bench if bench else []
        self.elixir = elixir
        self.shop = shop if shop else []

    def __repr__(self):
        return (
            f"Elixir: {self.elixir}\n"
            f"Board: {self.board}\n"
            f"Bench: {self.bench}\n"
            f"Shop: {self.shop}"
        )
