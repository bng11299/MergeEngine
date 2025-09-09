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
                self.elixir -= cost
                self.board.place_unit(unit)
                print(f"Bought {unit}")

                # Refresh just this slot in the shop
                name = random.choice(self.unit_pool)
                attack = random.randint(3, 7)
                hp = random.randint(10, 20)
                self.current_shop[idx] = Unit(name, attack=attack, hp=hp)
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


if __name__ == "__main__":
    gm = GameManager()
    gm.next_round()  # start round 1
    while True:
        cmd = input("\nPress ENTER to go to next round (or q to quit): ").strip()
        if cmd.lower() == "q":
            break
        gm.next_round()
