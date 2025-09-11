# unit.py
from cards import CardLibrary

class Unit:
    def __init__(self, name: str, star: int = 1):
        data = CardLibrary.get_card_data(name)
        self.name = name
        self.card_level = data["card_level"]
        self.star = star
        self.cost = data["cost"]
        self.traits = list(data["traits"])
        
        # Base stats from registry
        self.base_hp = data["hp"]
        self.base_dps = data["dps"]
        self.hit_speed = data["hit_speed"]
        
        # Scale stats based on star
        self.hp = self.base_hp * (2 ** (star - 1))
        self.dps = self.base_dps * (2 ** (star - 1))

    def upgrade(self):
        self.star += 1
        self.hp *= 2
        self.dps *= 2

    def __repr__(self):
        return (f"{self.name} Lv{self.card_level} ★{self.star} "
                f"(HP={self.hp}, DPS={self.dps:.1f}, SPD={self.hit_speed}, Traits={self.traits})")




if __name__ == "__main__":
    u = Unit("Archer", attack=5, hp=12)
    print(u)
    u.upgrade()
    print("After upgrade:", u)
