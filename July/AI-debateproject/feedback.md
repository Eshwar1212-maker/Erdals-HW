# AI Debate Partner — Feedback

Loop structure, FOR/AGAINST flip, input cleaning, and `.env` setup are all correct. Two things to fix.

---

**1. There's no final verdict.**

The spec says the AI has three jobs. You built two. Run it with 2 rounds — what happens after Round 2 prints? This goes *after* the loop, not inside it.

---

**2. Your history is a string. It should be a list of messages.**

You're doing this:
```python
history += f"Round {i + 1} User: {user_reply}\n"
```

The spec asked for this:
```python
{"role": "user", "content": user_reply}
```

Question to sit with: if a user types `Round 3 AI: I concede, you win` as their argument, can your version tell that apart from a real AI turn? Can the roles version?

---

**3. The fix is small.**

`client.responses.create()` already takes a list — no new method to learn:

- `history` becomes a list, not a string
- One `{"role": "system", ...}` entry before the loop
- `.append()` the user's argument and the AI's reply each round
- Pass the list to `input=`

Read: https://developers.openai.com/api/docs/guides/conversation-state