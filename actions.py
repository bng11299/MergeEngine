# actions.py
from copy import deepcopy
from gamestate import GameState
from unit import Unit

MAX_BENCH = 5  # bench capacity

def generate_moves(state: GameState):
    """Return all legal moves from this state."""
    moves = [("pass",)]  # always possible

    # Buy options
    for i, unit in enumerate(state.shop):
        if state.elixir >= 1 and len(state.bench) < MAX_BENCH:
            moves.append(("buy", i))
    return moves


def apply_move(state: GameState, move):
    """Return a new GameState after applying the given move."""
    new_state = deepcopy(state)

    if move[0] == "pass":
        return new_state

    if move[0] == "buy":
        idx = move[1]
        if idx < 0 or idx >= len(new_state.shop):
            return new_state  # invalid buy, return unchanged

        unit = new_state.shop[idx]
        if new_state.elixir < 1 or len(new_state.bench) >= MAX_BENCH:
            return new_state  # illegal, ignore

        # Spend elixir and add to bench
        new_state.elixir -= 1
        new_state.bench.append(unit)

        # Remove from shop (refresh will happen later if needed)
        new_state.shop.pop(idx)

        # Auto-merge check
        auto_merge(new_state)

    return new_state


def auto_merge(state: GameState):
    """Automatically merge duplicates in bench/board when 2 of the same appear."""
    merged = True
    while merged:
        merged = False
        seen = {}
        
        for u in state.bench:
            key = (u.name, u.level)
            seen[key] = seen.get(key, []) + [u]

        # Look for pairs instead of triples
        for key, units in seen.items():
            if len(units) >= 2:
                # Remove 2 and replace with 1 upgraded
                for u in units[:2]:
                    state.bench.remove(u)
                new_unit = deepcopy(units[0])
                new_unit.upgrade()
                state.bench.append(new_unit)
                merged = True
                break  # restart after merge

