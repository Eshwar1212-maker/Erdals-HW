# # Task — Pokémon Move Lookup

# Copy this dictionary into your file:

# ```
# moves = {
#     "Pikachu": "thunderbolt",
#     "Charizard": "flamethrower",
#     "Blastoise": "hydro pump",
#     "Gengar": "shadow ball",
#     "Mewtwo": "psychic"
# }
# ```

# Write a function called `get_move(pokemon)` that takes a Pokémon name and returns their move. If the Pokémon isn't in the dictionary, return `"Pokémon not found!"`.

# Then write a while loop that asks the user for a Pokémon name, calls `get_move()`, and prints the result. Also keep a count of how many Pokémon the user looked up successfully. When they type `"quit"`, print the total and say goodbye.

# Expected output:
# ```
# Enter a Pokémon: Pikachu
# Pikachu's move is thunderbolt

# Enter a Pokémon: Snorlax
# Pokémon not found!

# Enter a Pokémon: Mewtwo
# Mewtwo's move is psychic

# Enter a Pokémon: quit
# You looked up 2 Pokémon.
# Goodbye!
# ```

# 💡 Hint: only count a lookup if the Pokémon was actually found.