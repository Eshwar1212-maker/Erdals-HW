#  Problem 1 — Animal Sounds

The concept: Looking up a key in a dictionary, then combining two pieces of info into one printed line.

Step 1 — Create a dictionary called animals that stores at least 5 animal names and the sound they make.
animals = {
    "dog": "woof",
    "cat": "meow",
    ...
}

Step 2 — Ask the user to enter an animal name.

Step 3 — If the animal is in the dictionary, print a sentence that uses both the animal name and its sound in one line, like:
A dog says woof!

If it's not in the dictionary, print "Unknown animal!"

Expected output:

Enter an animal: cat

A cat says meow!

Enter an animal: dragon

Unknown animal!

Hint: Use an f-string → f"A {name} says {sound}!"

# Problem 2

🔥 Challenge 1 — Temperature Converter

Ask the user to enter a temperature in Celsius. Convert it to Fahrenheit and print the result. Then ask if they want to convert another one. Keep going until they say "no".

Formula: F = (C * 9/5) + 32

Expected output:

Enter temp in Celsius: 100

That is 212.0 degrees Fahrenheit.

Convert another? yes

Enter temp in Celsius: 0

That is 32.0 degrees Fahrenheit.

Convert another? no

Goodbye!

# Problem 3

# Challenge 3 Number Guessing with Stats Tracker
The computer picks a random number 1–100. The user gets unlimited guesses but you track everything in a dictionary and print a full stats report at the end.

pythonstats = {
    "guesses": [],
    "total_attempts": 0,
    "won": False
}

Expected output:

Guess a number (1-100): 50

Too high!

Guess a number (1-100): 25

Too low!

Guess a number (1-100): 37

You got it!

--- Your Stats ---

Total attempts: 3

Your guesses: [50, 25, 37]

Won: True