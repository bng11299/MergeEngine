from unit import Unit

class Board:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        # grid will hold Units or None
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def place_unit(self, row: int, col: int, unit: Unit):
        """Place a unit. If same type + level exists, merge instead of stacking."""
        existing = self.grid[row][col]

        if existing is None:
            # empty cell → just place it
            self.grid[row][col] = unit
        elif existing.name == unit.name and existing.level == unit.level:
            # same unit type & level → merge
            existing.upgrade()
        else:
            raise ValueError(
                f"Cell ({row}, {col}) is occupied by {existing}, cannot place {unit}."
            )

    def remove_unit(self, row: int, col: int):
        """Remove a unit from the board"""
        if self.grid[row][col] is not None:
            self.grid[row][col] = None
        else:
            raise ValueError(f"No unit at ({row}, {col}) to remove.")

    def get_unit(self, row: int, col: int):
        """Return the unit at a given cell"""
        return self.grid[row][col]

    def __repr__(self):
        """Pretty-print the board"""
        result = ""
        for r in range(self.rows):
            row_str = []
            for c in range(self.cols):
                unit = self.grid[r][c]
                if unit is None:
                    row_str.append(" . ")
                else:
                    row_str.append(str(unit))
            result += " | ".join(row_str) + "\n"
        return result


if __name__ == "__main__":
    b = Board()
    archer1 = Unit("Archer", attack=5)
    archer2 = Unit("Archer", attack=5)
    b.place_unit(0, 0, archer1)
    print("After placing first archer:\n", b)
    b.place_unit(0, 0, archer2)  # should merge!
    print("After merging:\n", b)
