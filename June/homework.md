## Challenge 1 — Scramble a word

Import random. Ask the user for a word. Use random.shuffle() on a list of its letters and print the scrambled version.

Expected output:

Enter a word: python

Scrambled: h t n o y p

## Challenge 2 — Guess the original

Use your code from Challenge 1. After printing the scramble, ask the user to guess the original word. Print "Correct!" or "Wrong, the word was python."

Expected output:

Scrambled: h t n o y p

Guess the word: typhon

Wrong, the word was python.

## Challenge 3 — Keep guessing

Use your code from Challenge 2. Give the user 3 attempts. Each wrong guess prints "Try again!" and shows attempts remaining. If they get it right, print "You got it!"

Expected output:

Scrambled: h t n o y p

Guess the word: nothpy

Wrong! 2 attempts left.

Guess the word: python

You got it!

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
