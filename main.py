from board import Board
from unit import Unit

def test_merging_three():
    board = Board(rows=2, cols=3)

    # Place three Archers
    board.place_unit(Unit("Archer", attack=5, hp=10), 0, 0)
    board.place_unit(Unit("Archer", attack=5, hp=10), 0, 1)
    board.place_unit(Unit("Archer", attack=5, hp=10), 0, 2)

    print("=== After placing 3 Archers ===")
    print(board)


def test_merging_four():
    board = Board(rows=2, cols=3)

    # Place four Archers
    board.place_unit(Unit("Archer", attack=5, hp=10), 0, 0)
    board.place_unit(Unit("Archer", attack=5, hp=10), 0, 1)
    board.place_unit(Unit("Archer", attack=5, hp=10), 0, 2)
    board.place_unit(Unit("Archer", attack=5, hp=10), 1, 0)

    print("\n=== After placing 4 Archers ===")
    print(board)


if __name__ == "__main__":
    test_merging_three()
    test_merging_four()