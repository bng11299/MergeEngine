import actions
print("Actions module contents:", dir(actions))

# test_actions.py
from gamestate import GameState
from unit import Unit
from actions import generate_moves, apply_move

def main():
    # Setup a simple state
    shop = [Unit("Archer", attack=2, hp=2),
            Unit("Knight", attack=3, hp=6),
            Unit("Archer", attack=2, hp=2)]
    state = GameState(board=[], bench=[], elixir=3, shop=shop)

    print("=== Initial State ===")
    print(state)

    # Show possible moves
    moves = generate_moves(state)
    print("\nPossible moves:")
    for m in moves:
        print(m)

    # Apply buying Archer (index 0)
    new_state = apply_move(state, ("buy", 0))
    print("\n=== After Buying First Archer ===")
    print(new_state)

    # Apply buying Archer again (index 1, since shop shifted)
    new_state2 = apply_move(new_state, ("buy", 1))
    print("\n=== After Buying Second Archer ===")
    print(new_state2)

    # Apply buying Knight (index 0 now)
    new_state3 = apply_move(new_state2, ("buy", 0))
    print("\n=== After Buying Knight (should trigger merge if 3 Archers exist) ===")
    print(new_state3)

if __name__ == "__main__":
    main()
