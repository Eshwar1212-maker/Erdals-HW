# Problem 1 — Your Favorite Foods

The concept: Making a dictionary and looking things up in it.

Step 1 — Create a dictionary called foods that stores at least 4 food names and your rating for each (a number from 1–10).

foods = {
    "pizza": 10,
    "broccoli": 4,
    ...
}
add three more

Step 2 — Ask the user to enter a food name with input().

Step 3 — Check if that food is in the dictionary.

If it is, print "Rating: " and the number.

If it isn't, print "I don't know that food!"

Expected output:

Enter a food: pizza
Rating: 10

Enter a food: sushi
I don't know that food!

#  Problem 2 — Animal Sounds

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
