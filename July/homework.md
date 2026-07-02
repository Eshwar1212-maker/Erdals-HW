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

## Feedback on the problem assignment earliar

🔴 Bug #1 — Lines 20-21: Points aren't actually updating

pythonpoints + bet   # ❌ this calculates but throws it away

Should be:

pythonpoints += bet  # ✅

Same problem on line 25 — points - bet needs to be points -= bet

🔴 Bug #2 — Structure is broken (the while True and while points > 0 are disconnected)

The betting loop (lines 7-13) and the game loop (lines 15-27) are two completely separate while blocks sitting next to each other — they're not nested or connected at all. The bet gets asked ONCE before the game even starts, then the game loop runs forever with that same bet. They need to be merged into one single loop.

🔴 Bug #3 — The guess is asked ONCE on line 5 outside any loop

So the user only ever guesses once at the very beginning, then the game just keeps flipping with that same guess forever. The input("Guess heads or tails") needs to be INSIDE the main loop.

✅ What IS good:

import random ✅

points = 100 starting point ✅

random.choice(["heads", "tails"]) correct ✅

Bet validation logic (if bet > points) — the RIGHT idea, just in the wrong place ✅