# House Search Generator

A simple Python script for generating random house encounters in tabletop RPG games, specifically designed for D&D campaigns set in Barovia or similar gothic horror settings.

## Description

This script simulates searching a house by rolling a d20 and determining what occupants (if any) are found inside. The encounters range from empty houses to dangerous undead, making it perfect for adding unpredictability to your gaming sessions.

## Features

- **Random d20 Roll**: Uses Python's random module to simulate dice rolls
- **Weighted Encounters**: Different probability ranges for various encounter types
- **2d4 Dice Mechanics**: Rat swarms and zombie encounters use two 4-sided dice for realistic distribution (2-8 range with bell curve)
- **Modular Design**: Function returns roll result for easy integration with other scripts
- **Clean Output**: Displays both the dice roll and the encounter result
- **Standalone or Import**: Can be run directly or imported as a module

## Encounter Table

| d20 Roll | Encounter | Probability |
|----------|-----------|-------------|
| 1-3      | Empty house | 15% |
| 4-8      | 2-8 Rat swarms | 25% |
| 9-16     | Barovian Villagers | 40% |
| 17-20    | 2-8 Strahd zombies | 20% |

## Installation

1. Ensure you have Python 3.x installed on your system
2. Download or clone this repository
3. No additional dependencies required (uses only Python standard library)

## Usage

### Running the Script

```bash
python house_search.py
```

### Using as a Module

```python
from house_search import search_house

# Generate a single encounter
result = search_house()
print(f"Dice roll was: {result}")
```

### Example Output

```
You rolled a d20 and got 14
Occupants: Barovian Villagers
```

```
You rolled a d20 and got 19
Occupants: 6 Strahd zombies
```

## Dice Mechanics

### Primary Roll (d20)
The main encounter determination uses a standard 20-sided die with weighted probability ranges.

### Variable Encounters (2d4)
- **Rat Swarms**: Uses 2d4 (range 2-8, average 5)
- **Strahd Zombies**: Uses 2d4 (range 2-8, average 5)

The 2d4 system creates a bell curve distribution where middle values (4-6) are more likely than extremes (2 or 8), making encounters feel more balanced while still allowing for dramatic variance.

| 2d4 Result | Probability |
|------------|-------------|
| 2 | 6.25% |
| 3 | 12.5% |
| 4 | 18.75% |
| 5 | 25% |
| 6 | 18.75% |
| 7 | 12.5% |
| 8 | 6.25% |

The script contains:
- `search_house()`: Main function that handles the dice roll and encounter logic
- Random number generation for both the main d20 roll and additional dice for variable encounters
- Conditional logic for different encounter types
- Return value for integration with other scripts

## Advanced Customization

### Creating Custom Encounter Tables

```python
def search_dungeon():
    """Alternative encounter table for dungeon exploration"""
    roll_result = random.randint(1, 20)
    print(f"You rolled a d20 and got {roll_result}")
    
    if 1 <= roll_result <= 5:
        print("Occupants: Empty chamber")
    elif 6 <= roll_result <= 10:
        num_skeletons = random.randint(1, 6)
        print(f"Occupants: {num_skeletons} skeletons")
    elif 11 <= roll_result <= 15:
        print("Occupants: Treasure chest (trapped)")
    elif 16 <= roll_result <= 20:
        print("Occupants: Ancient guardian")
    
    return roll_result
```

### Weighted Random Alternative

```python
import random

def weighted_search_house():
    """Uses weighted choices for more complex probability control"""
    encounters = [
        ("None", 15),
        ("Rats", 25), 
        ("Villagers", 40),
        ("Zombies", 20)
    ]
    
    encounter = random.choices(
        [e[0] for e in encounters],
        weights=[e[1] for e in encounters]
    )[0]
    
    return encounter
```

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional encounter types
- Configuration file support
- GUI interface
- Multiple encounter tables

## License

This project is open source. Feel free to use and modify for your tabletop gaming needs.

## Credits

Designed for use with D&D 5e and Curse of Strahd campaign settings, but adaptable to any gothic horror or fantasy RPG system.