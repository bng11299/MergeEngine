# game_manager.py
import random
from unit import Unit
from board import Board

class GameManager:
    def __init__(self):
        self.board = Board()
        self.elixir = 0
        self.round = 0
        self.shop_size = 3
        self.unit_pool = ["Archer", "Knight", "Mage"]  # placeholder
        self.current_shop = []

    def next_round(self):
        """Progress round, update board, and add elixir."""
        self.round += 1
        self.elixir += 4
        self.board.next_round()

        # auto-move units from bench if slots are free
        self.move_from_bench_to_board()

        # auto-merge across board + bench at start of round
        self.auto_merge_all()

        if not self.current_shop:  # only roll if empty
            self.roll_shop()

        print(f"\n=== ROUND {self.round} ===")
        self.show_status()
        self.shop_phase()


    def roll_shop(self):
        """Generate new shop units."""
        self.current_shop = []
        for _ in range(self.shop_size):
            name = random.choice(self.unit_pool)
            attack = random.randint(3, 7)
            hp = random.randint(10, 20)
            self.current_shop.append(Unit(name, attack=attack, hp=hp))

    def buy_unit(self, idx: int):
        """Buy a unit from the shop by index. Refreshes that slot."""
        if 0 <= idx < len(self.current_shop):
            cost = 2  # elixir per unit
            if self.elixir >= cost:
                unit = self.current_shop[idx]

                # try placing
                placed = False
                if len(self.board.units) < self.board.max_units:
                    self.board.place_unit(unit)
                    print(f"Bought {unit} → placed on board")
                    placed = True
                elif len(self.bench) < self.bench_capacity:
                    self.add_to_bench(unit)
                    print(f"Bought {unit} → placed on bench")
                    placed = True
                else:
                    print("Both board and bench are full! Cannot buy this unit.")
                    return  # don’t deduct elixir or refresh shop

                # if placed, spend elixir + refresh shop slot
                if placed:
                    self.elixir -= cost

                    # refresh this shop slot
                    name = random.choice(self.unit_pool)
                    attack = random.randint(3, 7)
                    hp = random.randint(10, 20)
                    self.current_shop[idx] = Unit(name, attack=attack, hp=hp)

                    # run full merge check
                    self.auto_merge_all()

            else:
                print("Not enough elixir!")
        else:
            print("Invalid shop index!")


    def shop_phase(self):
        """Interactive shop phase."""
        while True:
            print("\nSHOP:")
            for i, u in enumerate(self.current_shop, 1):
                print(f" {i}. {u} (Cost: 2 elixir)")

            print("\nCommands: [1-3]=buy, ENTER=done")
            choice = input("Your choice: ").strip().lower()

            if choice == "":
                break
            elif choice.isdigit():
                self.buy_unit(int(choice) - 1)
            else:
                print("Invalid choice.")

    def show_status(self):
        print(f"Elixir: {self.elixir}")
        print(f"Round: {self.round}, Max units: {self.board.max_units}")
        print(self.board)
    
    def add_to_bench(self, unit: Unit):
        """Add a unit to the bench if space allows."""
        if len(self.bench) < self.board.max_units:
            self.bench.append(unit)
            print(f"Added {unit} to bench.")
        else:
            print("Bench is full!")
    
    def move_from_bench_to_board(self, bench_idx: int, board_idx: int):
        """Move a unit from the bench to the board."""
        free_slots = self.board.max_units - len(self.board.units)
        moved = 0
        while free_slots > 0 and self.bench:
            unit = self.bench.pop(0)  # take leftmost unit
            self.board.place_unit(unit)  # will auto-merge if needed
            print(f"Moved {unit} from bench to board.")
            free_slots -= 1
            moved += 1
        if moved == 0:
            print("No units moved from bench to board.")


if __name__ == "__main__":
    gm = GameManager()
    gm.next_round()  # start round 1
    while True:
        cmd = input("\nPress ENTER to go to next round (or q to quit): ").strip()
        if cmd.lower() == "q":
            break
        gm.next_round()
