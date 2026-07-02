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

## Challenge: Coin Flip Bet 🎰

Start with 100 points. Each round, guess heads or tails AND bet some points. Win the bet if you're right, lose it if you're wrong. Game ends when you quit OR hit 0 points.

Hints:

Use random.choice(["heads", "tails"]) for the flip

Check if the bet is more than their points — if so, print "You don't have enough points!" and ask again

If points hit 0, end automatically

Expected Output:

```

You have 100 points.
Heads or tails? heads
How much do you bet? 20
Correct! You win 20 points.

You have 120 points.
Heads or tails? tails
How much do you bet? 50
Wrong! You lose 50 points.

You have 70 points.
Heads or tails? quit

--- Final Stats ---
Final points: 70

```