
## Challenge 1 

Ask the user for a number. Use a while loop to count down to 0.

Expected output:

Enter a number: 5

5

4

3

2

1

Done!

## Challenge 2

Use a while loop to keep asking the user for numbers and add them to a running total. Stop when they type "done" and print the total.

Expected output:

Enter a number (or done): 5

Enter a number (or done): 10

Enter a number (or done): 3

Enter a number (or done): done

Total: 18

## Challenge 3

Challenge 9 — Number Collector

Use a while loop to keep asking the user for numbers. Add each one to a list. Stop when they type "done" and print the full list.

Expected output:

Enter a number (or done): 4

Enter a number (or done): 7

Enter a number (or done): 2

Enter a number (or done): done

Your numbers: [4, 7, 2]


## Challenge 4

Ask the user for a word and a letter. Use a for loop with range(len(word)) to check each position. Print every index where the letter was found.

Expected output:

Enter a word: banana

Enter a letter: a

Found at index 1

Found at index 3

Found at index 5

## Challenge 5

Store the word "cat". Create a display list with underscores using ["_"] * len(word). Ask the user for a letter, reveal any matches, then print the updated display.

Expected output:

_ _ _
Guess a letter: a
_ a _

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
