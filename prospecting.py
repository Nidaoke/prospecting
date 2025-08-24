import math
import time
from typing import List, Tuple

class Item:
    def __init__(self, name: str, id: int, item_type: str, luck: int, capacity: int, 
                 dig_strength: float, dig_speed: float, shake_strength: float, shake_speed: float,
                 sell_boost: float, size_boost: float, modifier_boost: float):
        self.name = name
        self.id = id
        self.type = item_type
        self.luck = luck
        self.capacity = capacity
        self.dig_strength = dig_strength
        self.dig_speed = dig_speed
        self.shake_strength = shake_strength
        self.shake_speed = shake_speed
        self.sell_boost = sell_boost
        self.size_boost = size_boost
        self.modifier_boost = modifier_boost
    
    def __str__(self):
        return f"{self.name} ({self.type})"
    
    def __repr__(self):
        return self.__str__()

items = [
    # Key: (name, id, type, luck, capacity, dig_strength, dig_speed, shake_strength, shake_speed, sell_boost, size_boost, modifier_boost)

    # Pendants
    Item("Frosthorn Pendant 6*", 1, "pendant", 450, 225, 215, -.28, 0, 0, 0, 1.1,  0),
    Item("Phoenix Heart 6*",     2, "pendant", 325, 0,   0,   0,    0, 0, 0, -.35, 0),
    Item("Celestial Rings 6*",   3, "pendant", 100, 250, 0,   0,    0, 0, 0, .5,   1.5),
    Item("Frosthorn Pendant 5*", 4, "pendant", 400, 200, 200, -.3,  0, 0, 0, 1,    0),
    Item("Phoenix Heart 5*",     5, "pendant", 300, 0,   0,   0,    0, 0, 0, -.4,  0),
    Item("Celestial Rings 5*",   6, "pendant", 90,  250, 0,   0,    0, 0, 0, .45,  1.4),

    # Charms
    Item("Cryogenic Preserver 6*",    7,   "charm", 275, 0,   0, 0, 45, -.18, .55, 0,   0),
    Item("Fossilized Crown 6*",       8,   "charm", 260, 225, 0, 0, 0,  .32,  1.1, .55, 0),
    Item("Phoenix Wings 6*",          9,   "charm", 325, -45, 0, 0, 0,  0,    0,   0,   0),
    Item("Royal Federation Crown 6*", 10,  "charm", 100,  0,  0, 0, 0,  0,    2,   1,   0),
    Item("Cryogenic Preserver 5*",    11,  "charm", 275, 0,   0, 0, 45, -.18, .55, 0,   0),
    Item("Fossilized Crown 5*",       12,  "charm", 260, 225, 0, 0, 0,  .32,  1.1, .55, 0),
    Item("Phoenix Wings 5*",          13,  "charm", 325, -45, 0, 0, 0,  0,    0,   0,   0),
    Item("Royal Federation Crown 5*", 14,  "charm", 100,  0,  0, 0, 0,  0,    2,   1,   0),

    # Rings
    Item("Apocalypse Bringer 6*", 15, "ring", 45,  0,   22, 0,    5.5,  0,    .55,  0,   0),
    Item("Mythril Ring 6*",       16, "ring", 90,  0,   0,  .42,  0,    .42,  .26,  0,   0),
    Item("Prismatic Star 6*",     17, "ring", 22,  45,  11, .22,  3.2,  .22,  .22,  .22, .22),
    Item("Solar Ring 6*",         18, "ring", 110, 0,   9,  -.08, 2.2,  -.08, 0,    0,   .22),
    Item("Vortex Ring 6*",        19, "ring", 155, 325, 90, 0,    11,   0,    0,    0,   0),
    Item("Apocalypse Bringer 5*", 20, "ring", 40,  0,   20, 0,    5,    0,    .5,   0,   0),
    Item("Mythril Ring 5*",       21, "ring", 80,  0,   0,  .4,   0,    .4,   .24,  0,   0),
    Item("Prismatic Star 5*",     22, "ring", 20,  40,  10, .2,   3,    .2,   .2,   .2,  .2),
    Item("Solar Ring 5*",         23, "ring", 100, 0,   8,  -.1,  2,    -.1,  0,    0,   .2),
    Item("Vortex Ring 5*",        24, "ring", 140, 300, 80, 0,    10,   0,    0,    0,   0),

    # Pans
    Item("Frostbite Pan", 25, "pan", 300, 250, 0, 0, 15, .8, 0, 0, 0),
    Item("Galactic Pan",  26, "pan", 100, 500, 0, 0, 25, 1,  0, 0, 0),

    # Shovels
    Item("Icebreaker",      27, "shovel", 0, 0, 60, 1.1, 0, 0, 0, 0, 0),
    Item("Galactic Shovel", 28, "shovel", 0, 0, 60, .8,  0, 0, 0, 0, 0),

    # Enchants
    Item("Prismatic", 29, "enchant", 10, 20,  0, 0, 2, .1, 0, .1, .1),
    Item("Infernal",  30, "enchant", 80, -20, 0, 0, 0, 0,  0, -.1, 0),
    Item("Cosmic",    31, "enchant", 0,  50,  0, 0, 3, 0,  0, .25, 0),
    Item("Divine",    32, "enchant", 20, 40,  0, 0, 0, 0,  0, 0,   0)
]

def getGearOptions():
    print("\nBelow is a list of default gear to include.")
    print("Default Gear: {")
    print("  Pendants: Frosthorn Pendant 6*")
    print("  Charms: Cryogenic Preserver 6*, Fossilized Crown 6*")
    print("  Rings: Apocalypse Bringer 6*, Mythril Ring 6*, Prismatic Star 6*, Solar Ring 6*, Vortex Ring 6*")
    print("  Pans: Frostbite Pan, Galactic Pan")
    print("  Shovels: Icebreaker")
    print("  Enchants: Prismatic, Infernal, Cosmic, Divine")
    print("}")
    print("\nHit enter or 'y' to accept default.")
    print("Enter 'n' will allow you to customize the gear considered. (Note - number of each ring is a separate step coming up)")

    user_input = input("  Use default gear? (y/n): ").strip().lower()
    if user_input == 'n':
        print("\nFull Gear List: {")
        for item in items:
            print(f"  {item.id}: {item.name} ({item.type})")
        print("}")

        print("\nType a space separated list of gear IDs to include (1 7 8 15 16), the more items the slower the script:")
        user_input = input("  Enter gear IDs: ").strip()
        if user_input:
            return list(map(int, user_input.split()))
    return [1, 7, 8, 15, 16, 17, 18, 19, 25, 26, 27, 29, 30, 31, 32] # Default Gear IDs

def getLuckOptions():
    print("\nHow many builds would you like to see? (type number amount and press enter, default: 5)")
    numOfBuilds = int(input("  Enter number of builds: ").strip() or 5)

    print("\nSet constants here (press enter to leave constant as default)")
    digConstant = float(input("  Enter 1/digspeed -> seconds factor (default 2.1): ").strip() or 2.1)
    shakeConstant = float(input("  Enter 1/shakespeed -> seconds factor (default .37): ").strip() or .37)
    timeConstant = float(input("  Enter additive time constant (default 4.7): ").strip() or 4.7)

    print("\nHow many ring slots do you have available (default: 8)?")
    ringSlots = int(input("  Ring Slots: ") or 8)

    gearList = getGearOptions()
    maxRings = []

    print("\nFor each ring, enter the max number that should be allowed in the build (or hit enter to allow any amount)")
    for gid in gearList:
        gear = next((item for item in items if item.id == gid and item.type == "ring"), None)
        if gear:
            maxRings.append((gear.id, input(f"  {gear.name}: ") or ringSlots))

    print("\nEnter any stat modifications")
    statMods = [
        int(input("  Luck (default 33): ") or 33),
        int(input("  Capacity (default 25): ") or 25),
        int(input("  Dig Strength (default 5): ") or 5),
        int(input("  Dig Speed (default: 0) ") or 0),
        int(input("  Shake Strength (default 0): ") or 0),
        int(input("  Shake Speed (default 0): ") or 0)
    ]

    return [numOfBuilds, digConstant, shakeConstant, timeConstant, ringSlots, gearList, maxRings, statMods]

def template_money():
    print("Not yet available (btw, will never be 100% accurate until dev confirms how modifier boost works)")

def menu():
    print("-----------------------------------------------------------------------------------------------------")
    print("Welcome to Nidolya's Prospecting Tool! What would you like to do? (type number entry and press enter)")
    print("1. Show most optimal luck efficiency builds [default]")
    print("2. Show most optimal money efficiency builds (not fully accurate)")
    return int(input("  Enter your choice: ").strip() or 1)

def generate_ring_combinations(ring_max_list: List[Tuple[Item, int]], total_rings: int):
    def backtrack(index, current, remaining):
        if remaining == 0:
            yield tuple(current)
            return
        if index >= len(ring_max_list):
            return
        ring, max_count = ring_max_list[index]
        for count in range(0, min(max_count, remaining) + 1):
            current.extend([ring] * count)
            yield from backtrack(index + 1, current, remaining - count)
            for _ in range(count):
                current.pop()
    yield from backtrack(0, [], total_rings)

def calculate_luck_efficiency(items_combination: List[Item], stat_mods, dig_constant, shake_constant, time_constant) -> float:
    total_luck = sum(item.luck for item in items_combination) + stat_mods[0]
    total_capacity = sum(item.capacity for item in items_combination) + stat_mods[1]
    total_dig_strength = sum(item.dig_strength for item in items_combination) + stat_mods[2]
    total_dig_speed = sum(item.dig_speed for item in items_combination) + stat_mods[3]
    total_shake_strength = sum(item.shake_strength for item in items_combination) + stat_mods[4]
    total_shake_speed = sum(item.shake_speed for item in items_combination) + stat_mods[5]

    numerator = total_luck * math.sqrt(total_capacity) * .625

    dig_component = (dig_constant * math.ceil(total_capacity / (max(.0001, total_dig_strength * 1.5)))) / max(.0001, total_dig_speed)
    shake_component = (shake_constant * math.ceil(total_capacity / max(.0001, total_shake_strength))) / max(.0001, total_shake_speed)
    denominator = dig_component + shake_component + time_constant
    
    return numerator / max(.0001, denominator)

def find_best_combinations(items: List[Item], ring_slots, max_rings, stat_mods, dig_constant, shake_constant, time_constant, num_of_builds) -> List[Tuple[List[Item], float]]:
    pendants = [item for item in items if item.type == "pendant"]
    charms = [item for item in items if item.type == "charm"]
    rings = [item for item in items if item.type == "ring"]
    pans = [item for item in items if item.type == "pan"]
    shovels = [item for item in items if item.type == "shovel"]
    enchants = [item for item in items if item.type == "enchant"]

    combinations = []

    ring_max_list = [(next(item for item in rings if item.id == gid), int(max_count)) for gid, max_count in max_rings]
    # Convert generator to list so it can be iterated multiple times
    ring_combinations = list(generate_ring_combinations(ring_max_list, ring_slots))

    total_permutations = (
        len(pendants) *
        len(charms) *
        len(pans) *
        len(shovels) *
        len(enchants) *
        len(ring_combinations)
    )
    print(f"Total permutations to evaluate: {total_permutations}")

    calculations = 0
    start_time = time.time()

    for pendant in pendants:
        for charm in charms:
            for pan in pans:
                for shovel in shovels:
                    for enchant in enchants:
                        for ring_combination in ring_combinations:
                            combination = [pendant, charm, pan, shovel, enchant] + list(ring_combination)
                            luck_efficiency = calculate_luck_efficiency(combination, stat_mods, dig_constant, shake_constant, time_constant)

                            calculations += 1
                            percent_done = calculations / total_permutations
                            if total_permutations > 0 and calculations % max(1, total_permutations // 100) == 0:
                              elapsed = time.time() - start_time
                              print(f"Progress: {percent_done:.1%} ({calculations}/{total_permutations}) - Elapsed: {elapsed:.2f}s")
                            
                            if luck_efficiency > 0:
                                combinations.append((combination, luck_efficiency))

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Evaluated {calculations} combinations in {elapsed_time:.2f} seconds.")

    return combinations
    
def print_results(combinations: List[Tuple[List[Item], float]], stat_mods):
    """Print the top combinations in a readable format."""
    print("\nTOP 5 ITEM COMBINATIONS:")
    print("=" * 50)

    for i, (combination, luck_value) in enumerate(combinations, 1):
        print(f"\n#{i} - Luck Value: {luck_value:.4f}")
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
        total_luck = sum(item.luck for item in combination) + stat_mods[0]
        total_capacity = sum(item.capacity for item in combination) + stat_mods[1]
        total_dig_strength = sum(item.dig_strength for item in combination) + stat_mods[2]
        total_dig_speed = sum(item.dig_speed for item in combination) + stat_mods[3]
        total_shake_strength = sum(item.shake_strength for item in combination) + stat_mods[4]
        total_shake_speed = sum(item.shake_speed for item in combination) + stat_mods[5]
        
        print(f"Totals: Luck={total_luck}, Capacity={total_capacity}, \n"
              f"        Dig Str={total_dig_strength}, Dig Spd={total_dig_speed}, \n"
              f"        Shake Str={total_shake_strength}, Shake Spd={total_shake_speed}, \n")

def main():
    choice = menu()
    if choice == 1:
        (numOfBuilds, digConstant, shakeConstant, timeConstant, ringSlots, gearList, maxRings, statMods) = getLuckOptions()

        print(f"\nShowing the top {numOfBuilds} luck efficiency builds only including these items:")
        for gid in gearList:
            gear = next((item for item in items if item.id == gid), None)
            if gear:
                if gear.type == "ring":
                    for (i, j) in maxRings:
                        if gear.id == i:
                            print(f"  {gear.type}: {gear.name} (max: {j})")
                else:
                    print(f"  {gear.type}: {gear.name}")
        print(f"Using the equation:")
        print(f"                             Luck * sqrt(Capacity) * .625")
        print(f"--------------------------------------------------------------------------------------")
        print(f"({digConstant:.1f} * ⌈Capacity / (Dig Strength * 1.5)⌉) + ({shakeConstant:.2f} * ⌈Capacity / Shake Strength⌉)")
        print(f"-----------------------------------------   ------------------------------------ + {timeConstant}")
        print(f"                 Dig Speed                               Shake Speed")
        print("\n\n--------------------------------------------------------------------------------------")

        combinations = sorted(
            find_best_combinations(
                [item for item in items if item.id in gearList],
                ringSlots,
                maxRings,
                statMods,
                digConstant,
                shakeConstant,
                timeConstant,
                numOfBuilds
            ),
            key=lambda x: x[1], reverse=True
        )
        print_results(combinations[:numOfBuilds], statMods)

    elif choice == 2:
        template_money()
    else:
        print("Invalid choice. Please run the script again and choose 1 or 2.")

if __name__ == "__main__":
    main()