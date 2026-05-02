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