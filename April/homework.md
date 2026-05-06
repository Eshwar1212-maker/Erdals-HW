# Erdal HW — Hangman Build Week

## Use these sections in the Tech With Tim Video, watch the sections about arrays if you get confused 

https://www.youtube.com/watch?v=VchuKL44s6E

## Challenge 1 — Hangman: Starting the Hangman game (YOU ALREADY DID THIS!) 🙈
Create a new Python file called `hangman.py`.
Store a secret word. Print it out as underscores — one underscore for each letter in the word.

Expected output:
Secret word: apple
_ _ _ _ _

---

## Challenge 2 — Shopping List
Keep asking the user to add items until they type "done". Print the full list at the end.

Expected output:
Add item (or "done" to finish): apples
Add item (or "done" to finish): milk
Add item (or "done" to finish): bread
Add item (or "done" to finish): done
Your list: ['apples', 'milk', 'bread']

---

## Challenge 3 — Shopping List with Prices
Same shopping list but now ask for a price for each item too. Store the prices in a separate list. At the end print both lists AND the total cost.

Expected output:
Add item (or "done" to finish): apples
Price: 3
Add item (or "done" to finish): milk
Price: 2
Add item (or "done" to finish): done
Items: ['apples', 'milk']
Prices: [3, 2]
Total: $5

---

## Challenge 4 — Shopping List with a Budget
Same program but now ask the user for a budget at the start. After printing the total, tell them if they are under or over budget.

Expected output:
What is your budget? 4
Add item (or "done" to finish): apples
Price: 3
Add item (or "done" to finish): milk
Price: 2
Add item (or "done" to finish): done
Items: ['apples', 'milk']
Total: $5
You are $1 over budget!

---

## Challenge 5 — Hangman: Guess a Letter 🎯
Go back to `hangman.py`. Let the user guess one letter. Reveal it in the right spot if correct, print "Not in the word" if not.

Expected output:
_ _ _ _ _
Guess a letter: a
a _ _ _ _

Guess a letter: z
Not in the word.
_ _ _ _ _

## Challenge 5 — Grade Tracker


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