import random

# Wrap the whole logic inside the function
def search_house():
    roll_result = random.randint(1, 20)
    print(f"You rolled a d20 and got {roll_result}")

    if 1 <= roll_result <= 3:
        print("Occupants: None")
    elif 4 <= roll_result <= 8:
        num_rats = random.randint(1, 4) + random.randint(1, 4)
        print(f"Occupants: {num_rats} swarms of rats")
    elif 9 <= roll_result <= 16:
        print("Occupants: Barovian Villagers")
    elif 17 <= roll_result <= 20:
        num_zombies = random.randint(1, 4) + random.randint(1, 4)
        print(f"Occupants: {num_zombies} Strahd zombies")

    return roll_result  # ✅ Now this is inside the function

# Optional: run it when the script is called directly
if __name__ == "__main__":
    search_house()
