
# Challenge 1 — Environment Setup 🛠️

We just switched environments! Your code now lives in a shared repository with Eshwar — you are officially a collaborator. 🎉

**But there's a catch:** virtual environments (`venv` folders) don't travel with the repository. They only exist on the machine that created them. So when you cloned the repo, your `Trivia-Project` folder came WITHOUT a working virtual environment — which means `solution.py` will crash when you try to run it (missing packages like `openai`, `dotenv`, etc).

**Your mission:**
1. Create a brand new virtual environment inside the `Trivia-Project` folder
2. Activate it
3. Reinstall the packages your project needs
4. Get `solution.py` running again

Use AI (ChatGPT/Claude) to help you if you get stuck

You know you're done when: you can run `python solution.py` and the trivia game starts with no errors.

**Hints:**
- `python -m venv venv` creates a virtual environment
- Activating it is different on Windows vs Mac — look this up!
- `pip install openai python-dotenv` gets your packages back
- Don't forget: does your `.env` file with the API key exist in this folder? `.env` files also don't travel with repos (they're in `.gitignore` on purpose — never push API keys!)

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