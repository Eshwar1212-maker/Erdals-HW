````markdown
# 🗣️ AI Debate Partner

A Python terminal game where you pick a topic, choose your side, and go head-to-head in a debate against an AI — powered by the OpenAI API. The AI remembers everything you've said and fires back round after round. At the end, it judges who argued better.

---

## 🧠 Why This Project Matters

In your last two projects, every API call you made started fresh — the AI had no memory of what happened before. Each call was isolated.

This project changes that entirely.

Real AI conversations work by passing a **list of messages** to the API every single time — your messages, the AI's responses, all of it, in order. The AI isn't "remembering" anything on its own. You're the one keeping track of the conversation and sending the full history with each new request.

This list is called the **message history**, and it looks like this:

```python
messages = [
    {"role": "system", "content": "You are a debate opponent..."},
    {"role": "user", "content": "I think social media is good for society."},
    {"role": "assistant", "content": "That's a weak argument because..."},
    {"role": "user", "content": "But it connects people across the world!"},
]
```

Every time the user says something new, you append it to the list. Every time the AI responds, you append that too. Then you send the whole list to the API again. That's how the AI knows what's been said — because you told it.

This is the most important concept in this project. Everything else you already know how to do.

---

## 🎯 What It Does

- User picks a **debate topic** (anything — pineapple on pizza, school uniforms, social media, whatever)
- User picks their **side** (FOR or AGAINST)
- User picks **how many rounds** to debate
- Each round: user makes their argument, AI fires back
- The AI remembers every previous argument from both sides
- After all rounds, the AI gives a **final verdict** on who argued better
- The verdict is the AI's third job in this project

---

## 🕹️ Expected Output

````
Welcome to AI Debate Partner!
Debate topic: social media is good for society
Your side (FOR or AGAINST): FOR
How many rounds? 3

--- Round 1 ---
Your argument: Social media connects people across the world and lets us share ideas instantly.
AI: While connection sounds appealing, studies show

## Resources

Use this article to understand how to persist conversation memory and state:

- https://developers.openai.com/api/docs/guides/conversation-state
- https://medium.com/@Mustafa77/working-with-openai-api-part2-building-conversations-with-the-openai-api-a9974b3a96c8

