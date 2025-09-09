class Unit:
    def __init__(self, name: str, level: int = 1, attack: int = 1, hp: int = 10):
        self.name = name
        self.level = level
        self.attack = attack
        self.hp = hp

    def upgrade(self):
        """When merging, increase level and double attack + hp."""
        self.level += 1
        self.attack *= 2
        self.hp *= 2

    def __repr__(self):
        return f"{self.name}(Lv{self.level}, ATK={self.attack}, HP={self.hp})"


if __name__ == "__main__":
    u = Unit("Archer", attack=5, hp=12)
    print(u)
    u.upgrade()
    print("After upgrade:", u)
