from gamestate import GameState
from unit import Unit
from evaluate import evaluate

# make a test state
state = GameState(
    elixir=2,
    board=[Unit("Knight", 1, 3, 6)],
    bench=[Unit("Archer", 2, 4, 4)]
)

print("Score of state:", evaluate(state))
