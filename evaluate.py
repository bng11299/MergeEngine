# evaluate.py
from gamestate import GameState

def evaluate(state: GameState) -> int:
    """Return a score estimating how strong this game state is."""
    score = 0
    
    for unit in state.board + state.bench:
        # Base strength from stats
        score += unit.attack + unit.hp
        # Bonus for higher levels (encourages merging)
        score += unit.level * 5

    # Small bonus if we have leftover elixir (saves for future turns)
    score += state.elixir

    return score

# evaluate.py
def power_index(state):
    """Evaluate the state using board strength, health, elixir, etc."""

    # Trait multipliers (example numbers)
    trait_bonuses = {
        "Archer": {"attack_speed": 1.1},  # +10% attack speed
        "Knight": {"hp": 1.2},           # +20% HP
    }

    # Count traits on board
    trait_counts = {}
    for u in state.board:
        for t in getattr(u, "traits", []):
            trait_counts[t] = trait_counts.get(t, 0) + 1

    # Apply trait effects + compute unit contribution
    board_strength = 0
    for u in state.board:
        atk = u.attack
        hp = u.hp
        aspd = u.attack_speed

        for t in getattr(u, "traits", []):
            bonus = trait_bonuses.get(t, {})
            if "attack_speed" in bonus:
                aspd *= bonus["attack_speed"]
            if "hp" in bonus:
                hp *= bonus["hp"]

        dps = atk * aspd
        board_strength += dps + 0.5 * hp  # DPS more weighted than HP

    # Add player factors
    score = (
        1.0 * board_strength +
        0.5 * state.health +
        2.0 * state.elixir
    )

    return score

