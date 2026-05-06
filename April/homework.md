
## Challenge 6 — Grade Tracker

Ask the user to enter 5 test scores one by one using a `for i in range()` loop. Print all scores, the average, and whether they passed (average ≥ 60) or failed.

**Expected output:**
```
Enter score 1: 80
Enter score 2: 70
Enter score 3: 55
Enter score 4: 90
Enter score 5: 65
Scores: [80, 70, 55, 90, 65]
Average: 72.0
Result: Passed!
```

---

## Challenge 7 — Word Counter

Ask the user to type a sentence. Print the word count, then print each word numbered using `for i, word in enumerate()`.

**Expected output:**
```
Enter a sentence: I love coding in Python
Word count: 5
1. I
2. love
3. coding
4. in
5. Python
```

---

## Challenge 8 — Times Table Printer

Ask the user for a number. Print its full times table from 1–10 using `for i in range(1, 11)`.

**Expected output:**
```
Enter a number: 4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
```

## Challenge 9 — Hangman: Guess a Letter 🎯
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