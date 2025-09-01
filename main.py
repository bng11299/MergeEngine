from board import Board
from unit import Unit

b = Board()

# Place a new Archer unit for testing
archer = Unit("Archer", attack=5)
b.place_unit(0, 0, archer)

print("Now cell has:", b.grid[0][0].unit)

# Merge the unit
b.grid[0][0].unit.upgrade()
print("After upgrade:", b.grid[0][0].unit)
