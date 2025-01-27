def card_list():
    card_list = [
    # Plains (White)
    {"name": "Serra Angel", "mana_cost": {"white": 2, "blue": 0, "black": 0, "red": 0, "green": 0, "colorless": 3}, "power": 4, "toughness": 4, "abilities": ["Flying", "Vigilance"]},
    {"name": "Loxodon Smiter", "mana_cost": {"white": 1, "blue": 0, "black": 0, "red": 0, "green": 1, "colorless": 1}, "power": 4, "toughness": 4, "abilities": ["Cannot be countered"]},
    {"name": "Sun Titan", "mana_cost": {"white": 2, "blue": 0, "black": 0, "red": 0, "green": 0, "colorless": 4}, "power": 6, "toughness": 6, "abilities": ["Vigilance", "When it enters or attacks, return a permanent with mana cost 3 or less from your graveyard to the battlefield"]},
    
    # Island (Blue)
    {"name": "Snapcaster Mage", "mana_cost": {"white": 0, "blue": 1, "black": 0, "red": 0, "green": 0, "colorless": 1}, "power": 2, "toughness": 1, "abilities": ["Flash", "Target instant or sorcery in your graveyard gains flashback"]},
    {"name": "Aetherling", "mana_cost": {"white": 0, "blue": 2, "black": 0, "red": 0, "green": 0, "colorless": 4}, "power": 4, "toughness": 5, "abilities": ["{U}: Exile Aetherling, then return it to the battlefield under your control"]},
    {"name": "Thassa, God of the Sea", "mana_cost": {"white": 0, "blue": 1, "black": 0, "red": 0, "green": 0, "colorless": 2}, "power": 5, "toughness": 5, "abilities": ["Indestructible", "Scry 1 at the beginning of your upkeep"]},

    # Swamp (Black)
    {"name": "Grave Titan", "mana_cost": {"white": 0, "blue": 0, "black": 2, "red": 0, "green": 0, "colorless": 4}, "power": 6, "toughness": 6, "abilities": ["Deathtouch", "When it enters or attacks, create two 2/2 black Zombie creature tokens"]},
    {"name": "Bloodghast", "mana_cost": {"white": 0, "blue": 0, "black": 2, "red": 0, "green": 0, "colorless": 0}, "power": 2, "toughness": 1, "abilities": ["Cannot block", "Landfall: Return Bloodghast from your graveyard to the battlefield"]},
    {"name": "Phyrexian Obliterator", "mana_cost": {"white": 0, "blue": 0, "black": 4, "red": 0, "green": 0, "colorless": 0}, "power": 5, "toughness": 5, "abilities": ["Trample", "Whenever a source deals damage to Phyrexian Obliterator, that source's controller sacrifices that many permanents"]},

    # Mountain (Red)
    {"name": "Goblin Guide", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 1, "green": 0, "colorless": 0}, "power": 2, "toughness": 2, "abilities": ["Haste", "Whenever Goblin Guide attacks, defending player reveals the top card of their library"]},
    {"name": "Inferno Titan", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 2, "green": 0, "colorless": 4}, "power": 6, "toughness": 6, "abilities": ["Firebreathing", "When Inferno Titan enters or attacks, deal 3 damage divided as you choose"]},
    {"name": "Akroma, Angel of Fury", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 3, "green": 0, "colorless": 5}, "power": 6, "toughness": 6, "abilities": ["Flying", "Trample", "Protection from white and blue"]},

    # Forest (Green)
    {"name": "Llanowar Elves", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 0, "green": 1, "colorless": 0}, "power": 1, "toughness": 1, "abilities": ["{T}: Add {G}"]},
    {"name": "Craterhoof Behemoth", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 0, "green": 3, "colorless": 5}, "power": 5, "toughness": 5, "abilities": ["When Craterhoof Behemoth enters, creatures you control get +X/+X and trample"]},
    {"name": "Primeval Titan", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 0, "green": 2, "colorless": 4}, "power": 6, "toughness": 6, "abilities": ["Trample", "When Primeval Titan enters, search your library for two lands and put them onto the battlefield tapped"]},

    # Multicolor
    {"name": "Nicol Bolas, the Ravager", "mana_cost": {"white": 0, "blue": 1, "black": 1, "red": 1, "green": 0, "colorless": 1}, "power": 4, "toughness": 4, "abilities": ["Flying", "Transforms into a planeswalker"]},
    {"name": "Atraxa, Praetors' Voice", "mana_cost": {"white": 1, "blue": 1, "black": 1, "red": 0, "green": 1, "colorless": 0}, "power": 4, "toughness": 4, "abilities": ["Flying", "Vigilance", "Lifelink", "Proliferate"]},
    {"name": "Bloodbraid Elf", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 1, "green": 1, "colorless": 2}, "power": 3, "toughness": 2, "abilities": ["Haste", "Cascade"]},
    {"name": "Dragonlord Dromoka", "mana_cost": {"white": 1, "blue": 0, "black": 0, "red": 0, "green": 2, "colorless": 3}, "power": 5, "toughness": 7, "abilities": ["Flying", "Lifelink", "Your opponents can't cast spells during your turn"]},

    # Artifacts
    {"name": "Steel Hellkite", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 0, "green": 0, "colorless": 6}, "power": 5, "toughness": 5, "abilities": ["Flying", "{X}: Destroy each nonland permanent with mana cost X"]},
    {"name": "Blightsteel Colossus", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 0, "green": 0, "colorless": 12}, "power": 11, "toughness": 11, "abilities": ["Trample", "Infect", "Indestructible"]},
    {"name": "Solemn Simulacrum", "mana_cost": {"white": 0, "blue": 0, "black": 0, "red": 0, "green": 0, "colorless": 4}, "power": 2, "toughness": 2, "abilities": ["When Solemn Simulacrum enters, search for a basic land card", "When it dies, draw a card"]}

    ]
    
    return card_list 
