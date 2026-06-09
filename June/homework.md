## Intro to Python libraries and shuffle
Python has extra toolboxes you can bring into your code called libraries. To use one, you write import at the top of your file.
Today you're using one called random — it helps you do random things like shuffle and pick.

To bring it in, just write this at the very top:

pythonimport random

To shuffle a list, you do:

pythonrandom.shuffle(my_list)

That's it. Now go use it in the challenge.

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
