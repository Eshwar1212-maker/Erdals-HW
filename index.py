import random


pythonstats = {
    "guesses": [],
    "total_attempts": 0,
    "won": False
}

random_number = random_number = random.randint(1, 100)

while True:
    users_guess = input("Guess a number (1-100):")
    if users_guess == "quit":
        break
    users_guess = int(users_guess)
    pythonstats["guesses"].append(users_guess)
    pythonstats["total_attempts"] += 1
    if users_guess == random_number:
      pythonstats["won"] = True
    
    if users_guess < random_number:
      print("to low")
    
    if users_guess > random_number:
      print("to high")
    


print("--- Your Stats ---")

print("Total attempts: ", pythonstats["total_attempts"])

print("Your guesses: ",  pythonstats["guesses"])

print("Won:", pythonstats["won"])