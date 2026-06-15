# We are now diving into APIs and AI!

## Read these articles to understand what an API is

https://www.moesif.com/blog/technical/api-development/Python-API-Tutorial/

https://medium.com/@ritapossible/python-api-explained-916f2528d530

And watch this video

https://www.youtube.com/watch?v=hpc5jyVpUpw&t=42s

## Read this article to understand how to use Open AI's 

https://www.datacamp.com/tutorial/guide-to-openai-api-on-tutorial-best-practices

# Your AI Project

## Rock Paper Scissors with Skooby Doo

Build a Python program that lets a user play rock paper scissors with Skooby Do

Let a user guess "rock", "paper", or "scissors" and have the AI response also be an option between "rock", "paper", or "scissors".

Since the AI response will be from Skooby Do you must tell the AI in the instructions to act like him.

How would you do this? You would use the "input" and "instructions" variable in the "client.responses.create" you see in the documentation

Keep this program running until a user wins or loses. 

# Python Practice Problems

## Word Length Tracker

The computer picks a secret word from a list. The user keeps guessing words and you track everything in a dictionary. Type "quit" to stop and see the stats.

stats = {
    "guesses": [],
    "total_attempts": 0,
    "found": False
}


Expected output:
'''
Guess the word: python
Too long!
Guess the word: hi
Too short!
Guess the word: cat
You got it!

--- Your Stats ---
Total attempts: 3
Your guesses: ['python', 'hi', 'cat']
Found: True

'''

Hint: Use len() to compare word lengths instead of numeric comparisons.

## Coin Flip Streak

The computer flips a coin randomly each round. The user guesses "heads" or "tails". Track their streak and total results in a dictionary. Type "quit" to stop.

stats = {
    "guesses": [],
    "correct": 0,
    "wrong": 0,
    "longest_streak": 0
}

Expected output:
'''
Heads or tails? heads
Correct! It was heads.
Heads or tails? tails
Wrong! It was heads.
Heads or tails? quit

--- Your Stats ---
Correct: 1
Wrong: 1
Longest streak: 1
'''

Hint: Use random.choice(["heads", "tails"]) for the flip.