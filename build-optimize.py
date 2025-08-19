import math
from itertools import combinations, combinations_with_replacement
from typing import List, Dict, Tuple

class Item:
    def __init__(self, name: str, item_type: str, luck: int, capacity: int, 
                 dig_strength: int, dig_speed: int, shake_strength: int, shake_speed: int):
        self.name = name
        self.type = item_type
        self.luck = luck
        self.capacity = capacity
        self.dig_strength = dig_strength
        self.dig_speed = dig_speed
        self.shake_strength = shake_strength
        self.shake_speed = shake_speed
    
    def __str__(self):
        return f"{self.name} ({self.type})"
    
    def __repr__(self):
        return self.__str__()

def generate_ring_combinations(rings: List[Item], total_rings: int, max_per_ring: int = 4):
    """
    Generate all possible combinations of rings where we select total_rings rings,
    with no more than max_per_ring of any single ring type.
    """
    def backtrack(index, current_combination, remaining_rings):
        if remaining_rings == 0:
            yield current_combination[:]
            return
        
        if index >= len(rings) or remaining_rings < 0:
            return
        
        ring = rings[index]
        
        # Try using 0 to max_per_ring of this ring type
        for count in range(min(max_per_ring + 1, remaining_rings + 1)):
            current_combination.extend([ring] * count)
            yield from backtrack(index + 1, current_combination, remaining_rings - count)
            # Remove the rings we just added
            for _ in range(count):
                if current_combination:
                    current_combination.pop()
    
    yield from backtrack(0, [], total_rings)

items = [
    # Pendants
    Item("Phoenix Heart",     "pendant", 300, 0,   0,   0,   0, 0),
    #Item("Celestial Rings",   "pendant", 90,  250, 0,   0,   0, 0),
    #Item("Frosthorn Pendant", "pendant", 400, 200, 200, -.3, 0, 0),
    Item("Frosthorn Pendant 6*", "pendant", 450, 225, 215, -.28, 0, 0),
    
    # Charms
    #Item("Royal Federation Crown", "charm", 90,  0,   0, 0, 0,  0),
    Item("Phoenix Wings",          "charm", 300, -40, 0, 0, 0,  0),
    #Item("Cryogenic Preserver",    "charm", 250, 0,   0, 0, 40, -.2),
    Item("Cryogenic Preserver 6*",    "charm", 275, 0,   0, 0, 45, -.18),
    #Item("Fossilized Crown",       "charm", 250, 200, 0, 0, 0,  .3),
    Item("Fossilized Crown 6*",    "charm", 260, 225, 0, 0, 0,  .32),
    
    # Rings
    #Item("Apocalypse Bringer", "ring", 40,  0,  20, 0,   5, 0),
    #Item("Mythril Ring",       "ring", 80,  0,  0,  .4,  0, .4),
    #Item("Prismatic Star",     "ring", 20,  40, 10, .2,  3, .2),
    #Item("Solar Ring",         "ring", 100, 0,  8,  -.1, 2, -.1),
    Item("Apocalypse Bringer 6*", "ring", 45,  0,  22, 0,   5.5, 0),
    Item("Mythril Ring 6*",       "ring", 90,  0,  0,  .42,  0, .42),
    Item("Prismatic Star 6*",     "ring", 22,  45, 11, .22,  3.2, .22),
    Item("Solar Ring 6*",         "ring", 110, 0,  9,  -.08, 2.2, -.08),

    # Pans
    Item("Frostbite Pan",  "pan", 300, 250, 0, 0, 15, .8),
    #Item("Fossilized Pan", "pan", 200, 225, 0, 0, 8,  1),

    # Shovels
    #Item("Dragonflame Shovel", "shovel", 0, 0, 50, .6,  0, 0),
    Item("Icebreaker",         "shovel", 0, 0, 60, 1.1, 0, 0),

    # Enchants
    Item("Prismatic",   "enchant", 10, 20,  0, 0, 2, .1),
    Item("Infernal",    "enchant", 80, -20, 0, 0, 0, 0),
    Item("Cosmic",      "enchant", 0,  50,  0, 0, 3, 0),
    Item("Destructive", "enchant", 0,  0,   0, 0, 5, 0),
    Item("Divine",      "enchant", 20, 40,  0, 0, 0, 0),
]

def calculate_value(items_combination: List[Item]) -> float:
    """
    Calculate the value of a combination using the given formula:
    (Luck * sqrt(capacity) * .65) / ((((2.1 * ceil(capacity / (dig strength * 1.5)) ) / dig speed) + (((.37 * ceil(capacity / shake strength)) / shake speed)) + 4.7)
    """
    total_luck = sum(item.luck for item in items_combination) + 33
    total_capacity = sum(item.capacity for item in items_combination) + 25
    total_dig_strength = sum(item.dig_strength for item in items_combination) + 5
    total_dig_speed = sum(item.dig_speed for item in items_combination)
    total_shake_strength = sum(item.shake_strength for item in items_combination)
    total_shake_speed = sum(item.shake_speed for item in items_combination)

    if total_dig_speed <= 0:
        total_dig_speed = .001
    if total_shake_speed <= 0:
        total_shake_speed = .001
    if total_dig_strength <= 0:
        total_dig_strength = .001
    if total_shake_strength <= 0:
        total_shake_strength = .001

    # Calculate numerator
    numerator = total_luck * math.sqrt(total_capacity) * 0.65
    
    # Calculate denominator components
    dig_component = (2.1 * math.ceil(total_capacity / (total_dig_strength * 1.5))) / total_dig_speed
    shake_component = (0.37 * math.ceil(total_capacity / total_shake_strength)) / total_shake_speed
    denominator = dig_component + shake_component + 4.7
    
    return numerator / denominator

def find_best_combinations(items: List[Item]) -> List[Tuple[List[Item], float]]:
    """
    Find the best combinations of 1 pan, 1 enchant, 1 pendant, 1 charm, and 8 rings.
    Returns the top 5 combinations with their values.
    """
    # Separate items by type
    pendants = [item for item in items if item.type == "pendant"]
    charms = [item for item in items if item.type == "charm"]
    rings = [item for item in items if item.type == "ring"]
    pans = [item for item in items if item.type == "pan"]
    shovels = [item for item in items if item.type == "shovel"]
    enchants = [item for item in items if item.type == "enchant"]
    
    best_combinations = []
    
    # Try all combinations of 1 pan, 1 enchant, 1 pendant, 1 charm, and 8 rings (with repetition allowed, max 4 per ring)
    for shovel in shovels:
        for pan in pans:
            for enchant in enchants:
                for pendant in pendants:
                    for charm in charms:
                        # Use custom generator to allow duplicate rings with max 4 per ring type
                        #for ring_combination in generate_ring_combinations(rings, 8, max_per_ring=4):
                        for ring_combination in combinations_with_replacement(rings, 8):
                            combination = [pan, shovel, enchant, pendant, charm] + list(ring_combination)
                            value = calculate_value(combination)
                            best_combinations.append((combination, value))
    
    # Sort by value (descending) and return top 5
    best_combinations.sort(key=lambda x: x[1], reverse=True)
    return best_combinations[:5]

def print_results(combinations: List[Tuple[List[Item], float]]):
    """Print the top combinations in a readable format."""
    print("\nTOP 5 ITEM COMBINATIONS:")
    print("=" * 50)
    
    for i, (combination, value) in enumerate(combinations, 1):
        print(f"\n#{i} - Value: {value:.4f}")
        print("-" * 30)
        
        # Group by type for better readability
        pan = [item for item in combination if item.type == "pan"][0]
        shovel = [item for item in combination if item.type == "shovel"][0]
        enchant = [item for item in combination if item.type == "enchant"][0]
        pendant = [item for item in combination if item.type == "pendant"][0]
        charm = [item for item in combination if item.type == "charm"][0]
        rings = [item for item in combination if item.type == "ring"]
        
        print(f"Pan: {pan.name}")
        print(f"Shovel: {shovel.name}")
        print(f"Enchant: {enchant.name}")
        print(f"Pendant: {pendant.name}")
        print(f"Charm: {charm.name}")
        
        # Count ring occurrences for better display
        ring_counts = {}
        for ring in rings:
            ring_counts[ring.name] = ring_counts.get(ring.name, 0) + 1
        
        print("Rings:")
        for ring_name, count in ring_counts.items():
            if count > 1:
                print(f"  - {ring_name} x{count}")
            else:
                print(f"  - {ring_name}")
        
        # Print totals
        total_luck = sum(item.luck for item in combination)
        total_capacity = sum(item.capacity for item in combination)
        total_dig_strength = sum(item.dig_strength for item in combination)
        total_dig_speed = sum(item.dig_speed for item in combination)
        total_shake_strength = sum(item.shake_strength for item in combination)
        total_shake_speed = sum(item.shake_speed for item in combination)
        
        print(f"Totals: Luck={total_luck}, Capacity={total_capacity}, \n"
              f"        Dig Str={total_dig_strength}, Dig Spd={total_dig_speed}, \n"
              f"        Shake Str={total_shake_strength}, Shake Spd={total_shake_speed}")

if __name__ == "__main__":
    try:
        print("Finding optimal item combinations...")
        best_combinations = find_best_combinations(items)
        print_results(best_combinations)
    except Exception as e:
        print(f"Error: {e}")
