# board.py
from unit import Unit

class Board:
    def __init__(self, rows: int = 4, cols: int = 5):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.bench = []  # holds extra units
        self.round = 1
        self.max_units = 2  # starts at 2, increases each round up to 6

    def next_round(self):
        """Progress to the next round and increase max_units up to 6."""
        self.round += 1
        self.max_units = min(6, self.max_units + 1)
        self.autofill_from_bench()

    def count_units_on_board(self):
        return sum(1 for r in range(self.rows) for c in range(self.cols) if self.grid[r][c])

    def place_unit(self, unit: Unit, row: int = None, col: int = None):
        """Place unit either on board (if under cap) or on bench."""
        if self.count_units_on_board() < self.max_units:
            # find empty slot if row/col not specified
            if row is None or col is None:
                for r in range(self.rows):
                    for c in range(self.cols):
                        if self.grid[r][c] is None:
                            row, col = r, c
                            break
                    if row is not None:
                        break
            if self.grid[row][col] is None:
                self.grid[row][col] = unit
                self.auto_merge(unit.name)
                self.autofill_from_bench()
            else:
                raise ValueError(f"Cell ({row},{col}) is already occupied!")
        else:
            # cap reached → send to bench
            self.bench.append(unit)

    def auto_merge(self, unit_name: str):
        """Merge units of the same type immediately if 3+ exist."""
        units = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (u := self.grid[r][c]) and u.name == unit_name:
                    units.append((r, c, u))

        while len(units) >= 3:
            to_merge = units[:3]
            units = units[3:]
            r, c, u = to_merge[0]
            u.upgrade()
            for r2, c2, _ in to_merge[1:]:
                self.grid[r2][c2] = None
            self.grid[r][c] = u
            # re-collect
            units = []
            for r in range(self.rows):
                for c in range(self.cols):
                    if (u := self.grid[r][c]) and u.name == unit_name:
                        units.append((r, c, u))

    def autofill_from_bench(self):
        """Fill empty slots from bench until reaching max_units cap."""
        while self.bench and self.count_units_on_board() < self.max_units:
            unit = self.bench.pop(0)  # take leftmost
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.grid[r][c] is None:
                        self.grid[r][c] = unit
                        self.auto_merge(unit.name)
                        break
                else:
                    continue
                break

    def __repr__(self):
        rep = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if self.grid[r][c]:
                    row.append(str(self.grid[r][c]))
                else:
                    row.append(" . ")
            rep.append(" | ".join(row))
        rep.append(f"Bench: {self.bench}")
        return "\n".join(rep)


if __name__ == "__main__":
    b = Board()
    b.place_unit(Unit("Archer", attack=5))
    b.place_unit(Unit("Archer", attack=5))
    b.place_unit(Unit("Archer", attack=5))  # should go to bench since cap=2
    print(b)
    b.next_round()  # cap=3, autofill from bench
    print("After round 2:")
    print(b)
