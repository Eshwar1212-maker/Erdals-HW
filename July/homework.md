## Challenge 1 - Environment setup

We just switched environments! Your code is now shared together with Eshwar in the repository, you are now a collaborator. 

However this means if you run your existing Python file in 'Trivia-Project' it will not work because you have to reinstall the virtual environment.

This tasks goal is to reinstall the virtual environment in that folder and get your 'solution.py' File working so you can continue to work on your app.

Use AI ChatGPT/Claude to help you do this.
 

## Challenge 2: Word Frequency Counter 📝

Ask the user to type a sentence. Count how many times each word appears and store it in a dictionary. Print the results sorted from most to least frequent.

**Hints:**
- Use `.split()` to break the sentence into words
- Use `.lower()` to make it case-insensitive
- Use `word_count[word] = word_count.get(word, 0) + 1` to count
- Use `sorted()` with `key=lambda x: x[1], reverse=True` to sort

**Expected Output:**
```
Enter a sentence: the cat sat on the mat the cat sat

--- Word Frequencies ---
the → 3
cat → 2
sat → 2
on → 1
mat → 1

```

## Challenge 2(HARD): Blackjack Lite 🃏

Build a simplified Blackjack game. The deck has cards with these values:

```
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
```

Shuffle the deck and deal 2 cards to the player and 2 to the dealer (dealer's second card is hidden). Each round, ask the player "Hit or stand?". If they hit, deal another card. If their total exceeds 21, they bust. When they stand, reveal the dealer's hidden card — the dealer must keep hitting until their total is 17 or more. Highest total without busting wins.

**Hints:**
- Use `random.shuffle()` and `deck.pop()` to deal cards
- Use `sum()` to get totals
- Dealer logic goes in a `while` loop after the player stands

**Expected Output:**
```
Your cards: [10, 7] → Total: 17
Dealer shows: [9, ?]

Hit or stand? hit
You drew a 3 → Total: 20

Hit or stand? stand
Dealer reveals: [9, 6] → Total: 15
Dealer hits... draws 4 → Total: 19

Dealer wins! 🤖