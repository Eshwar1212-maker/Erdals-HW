## Python libraries and Shuffle

Python has extra toolboxes you can bring into your code called libraries. To use one, you write import at the top of your file.
Today you're using one called random — it helps you do random things like shuffle and pick.

To bring it in, just write this at the very top:

import random

To shuffle a list, you do:

pythonrandom.shuffle(my_list)

That's it. Now go use it in the challenge.

## Challenge 1

Ask the user for a word. Use a for loop with range(len(word)) 

to print each letter and its position number.

Expected output:

Enter a word: cat

Letter 0 is c

Letter 1 is a

Letter 2 is t

## Challenge 2

Ask the user for a word. Use enumerate to print each letter and its position number.

TAKE advantage of the fact enumerate gives you the index and the value of each position. 

Expected output:

Enter a word: cat

Letter 0 is c

Letter 1 is a

Letter 2 is t

## Challenge 3
Ask the user for their name and a letter. First check if the 

letter is even in the name using the "in" keyword. If it's not, 

print "Not found!" and stop. If it is, use a for loop with 

range(len(name)) to print every index where it was found.


Expected output:

Enter your name: Erdal

Enter a letter: a

Found at index 3


Enter your name: Erdal

Enter a letter: z

Not found!

## Challenge 4

Ask the user for a word. Use a while loop to keep asking them 

to guess a letter. After each guess, print every index where 

that letter was found. Stop when they type "done".

Expected output:

Enter a word: banana

Guess a letter: a

Found at index 1

Found at index 3

Found at index 5

Guess a letter: b

Found at index 0

Guess a letter: done

Goodbye!


## Hangman: Guess a Letter 🎯
Go back to your hangman.py file

Challenge 5 — Hangman: Guess a Letter 🎯

Step 1 — Create a variable called word and set it to any 5-letter string like "apple".

Step 2 — Create a list called display filled with underscores, one per letter. Use for i in range(len(word)).

Step 3 — Print display as a space-separated line using for letter in display.

Step 4 — Ask the user to guess a letter with input().

Step 5 — Loop through the word using for i in range(len(word)). If word[i] matches the guess, set display[i] to that letter.

Step 6 — If the guess wasn't found anywhere in the word, print "Not in the word."

Step 7 — Print display again to show the updated board.

Expected output:

_ _ _ _ _

Guess a letter: a

a _ _ _ _

Guess a letter: z

Not in the word.

a _ _ _ _
