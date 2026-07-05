# Python Practice Problems

# Question 1

### Look Up Values in a Dictionary

Step 1: Copy this dictionary into your file:

pythonpowers = { "Spider-Man": "web-slinging", "Thor": "lightning", "Hulk": "super strength" }

Step 2: Print out Thor's power directly using its key.

Step 3: Ask the user for a hero name with input(), then print that hero's power.

Expected output:

Thor's power is lightning

Enter a hero: Hulk Hulk's power is super strength


# Question 2

Build a quiz game. Store 5 questions and answers in a dictionary. Loop through every question, ask the user, and track everything in a stats dictionary.

pythonstats = { "answers_given": [], "correct": 0, "wrong": 0 }

After all 5 questions, print a full report.

Expected output:

What is the capital of France? Paris Correct!

What is 7 x 8? 56 Correct!

What color is the sky? green Wrong! The answer was blue.

--- Your Stats --- Total correct: 2 Total wrong: 1 Your answers: ['Paris', '56', 'green']

💡 Hints:

Store questions as keys, answers as values in one dictionary Loop through the dictionary with a for loop Append each user answer to answers_given whether right or wrong Compare .lower() versions so capitalization doesn't matter

# Question 3

```markdown
# Python Practice Problems

## Challenge: The Number Guessing Gauntlet 🏆

The computer picks a **secret number between 1 and 100**. The player has **7 attempts** to guess it. After each wrong guess, tell them if they're too high or too low AND how many attempts remain. If they guess right, they win. If they run out of guesses, game over — reveal the number.

**But here's the twist:** track a **score** that starts at 700 and drops by 100 each wrong guess. If they win, print their score. If they lose, score is 0.

**Hints:**
- Use `random.randint(1, 100)` to pick the number
- Use `int(input(...))` to get the guess
- Use a `while` loop with an attempts counter

**Expected Output:**

​```
🎯 Guess the secret number (1–100). You have 7 attempts!

Attempt 1: 50
Too low! 6 attempts left.

Attempt 2: 75
Too high! 5 attempts left.

Attempt 3: 63
Too low! 4 attempts left.

Attempt 4: 70
You got it! 🎉

--- Results ---
Score: 400
​```

**If they lose:**
​```
Out of attempts! The number was 63.

--- Results ---
Score: 0
​```
```