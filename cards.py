# cards.py
# cards.py

class CardLibrary:
    CARDS = {
        "Archers": {
            "cost": 2,
            "attack_speed": 1 / 1,  # convert hit speed
            "hp": 480,
            "dps": 84,
            "traits": ["Clan", "Ranger"],
            "card_level": 1
        },
        "Barbarians": {
            "cost": 2,
            "attack_speed": 1 / 1,  # convert hit speed
            "hp": 840,
            "dps": 96,
            "traits": ["Clan", "Brawler"],
            "card_level": 1
        },
        "Bomber": {
            "cost": 2,
            "attack_speed": 1 / 1.42,  # convert hit speed
            "hp": 480,
            "dps": 136.32,
            "traits": ["Undead", "Thrower"],
            "card_level": 1
        },
        "Goblins": {
            "cost": 2,
            "attack_speed": 1 / 0.71,  # convert hit speed
            "hp": 540,
            "dps": 68.16,
            "traits": ["Goblin", "Assassin"],
            "card_level": 1
        },
        "Knight": {
            "cost": 2,
            "attack_speed": 1 / 1.42,  # convert hit speed
            "hp": 1200,
            "dps": 85.2,
            "traits": ["Noble", "Juggernaut"],
            "card_level": 1
        },
        "Spear Goblin": {
            "cost": 2,
            "attack_speed": 1 / 1.6,  # convert hit speed
            "hp": 360,
            "dps": 211.2,
            "traits": ["Goblin", "Thrower"],
            "card_level": 1
        },
        "Dart Goblin": {
            "cost": 3,
            "attack_speed": 1 / .83,  # convert hit speed
            "hp": 534,
            "dps": 66.4,
            "traits": ["Goblin", "Ranger"],
            "card_level": 1
        },
        "Executioner": {
            "cost": 3,
            "attack_speed": 1 / 1,  # convert hit speed
            "hp": 763,
            "dps": 130, #axe comes back and deals damage again regardless of if he dies
            "traits": ["Ace", "Thrower"],
            "card_level": 1
        },
        "Giant Skeleton": {
            "cost": 3,
            "attack_speed": 1 / 1.66,  # convert hit speed
            "hp": 981,
            "dps": 89.64,
            "traits": ["Undead", "Brawler"],
            "card_level": 1
        },
        "P.E.K.K.A": {
            "cost": 3,
            "attack_speed": 1 / 2.5,  # convert hit speed
            "hp": 1309,
            "dps": 937.5,
            "traits": ["Ace", "Juggernaut"],
            "card_level": 1
        },
        "Prince": {
            "cost": 3,
            "attack_speed": 1 / 1.2,  # convert hit speed
            "hp": 872,
            "dps": 144,
            "traits": ["Noble", "Brawler"],
            "card_level": 1
        },
        "Valkyrie": {
            "cost": 3,
            "attack_speed": 1 / 1,  # convert hit speed
            "hp": 1369,
            "dps": 115, #swing 360 degrees around her, should adjust?
            "traits": ["Clan", "Avenger"],
            "card_level": 1
        },
        "Bandit": {
            "cost": 4,
            "traits": ["Ace", "Avenger"],
            "card_level": 1
        },
        "Goblin Machine": {
            "cost": 4,
            "traits": ["Goblin", "Juggernaut"],
            "card_level": 1
        },
        "Mega Knight": {
            "cost": 4,
            "attack_speed": 1 / 1.66,  # convert hit speed
            "hp": 1466,
            "dps": 58,
            "traits": ["Ace", "Brawler"],
            "card_level": 9,
        },
        "Princess": {
            "cost": 4,
            "traits": ["Noble", "Ranger"],
            "card_level": 1
        },
        "Royal Ghost": {
            "cost": 4,
            "attack_speed": 1.0,  # from stat "1.00 sec"
            "hp": 838,
            "dps": 127,           # DPS at star level 1
            "traits": ["Undead", "Assassin"],
            "card_level": 9,      # starting level shown
        },
        "Archer Queen": {
            "cost": 5,
            "traits": ["Clan", "Avenger"],
            "card_level": 1
        },
        "Golden Knight": {
            "cost": 5,
            "traits": ["Noble", "Assassin"],
            "card_level": 1
        },
        "Skeleton King": {
            "cost": 5,
            "traits": ["Undead", "Juggernaut"],
            "card_level": 1
        }
    }

    @classmethod
    def get(cls, name):
        card = cls.CARDS.get(name)
        if card is None:
            raise ValueError(f"Unknown card name: '{name}'")
        return card.copy()
