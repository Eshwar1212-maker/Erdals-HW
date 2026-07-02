# 🧠 AI Trivia Game

A Python terminal game where an AI generates trivia questions on ANY topic you choose, checks your answers, and tracks your score across multiple rounds — all powered by the OpenAI API.

---

## 🎯 What It Does

- User picks a **topic** (sports, anime, history, science — anything)
- User picks **how many rounds** to play
- AI generates a **unique trivia question** each round based on the topic
- User submits an answer
- AI **judges the answer** and says if it's right or wrong
- Score is tracked across all rounds
- Final results printed at the end

---

## 🕹️ Expected Output

```
What topic do you want? basketball
How many rounds? 3

--- Round 1 ---
Question: How many players from one team are on the court at a time in the NBA?
Your answer: 5
✅ Correct!
Score: 1/1

--- Round 2 ---
Question: Which player has the most career points in NBA history?
Your answer: lebron james
✅ Correct!
Score: 2/2

--- Round 3 ---
Question: What year did the Chicago Bulls win their first NBA championship?
Your answer: 1990
❌ Wrong! The correct answer was 1991.
Score: 2/3

--- Game Over ---
Final Score: 2/3
```

---

## 📁 Project Structure

```
trivia_project/
├── main.py       # All game logic lives here
├── .env          # Your OpenAI API key (never share this, you can use the same one you used for the Skooby Doo Project)
└── project-description.md     # This file
```

---

## 🛠️ Setup

### 1. Clone or create the project folder

```bash
mkdir trivia_project
cd trivia_project
```

### 2. Install dependencies

```bash
pip install openai python-dotenv
```

### 3. Create your `.env` file

```
OPENAI_API_KEY=your_key_here
```

> ⚠️ No quotes, no spaces around the `=` sign

### 4. Run it

```bash
python main.py
```

---

## 🧩 Concepts Used

| Concept | Where It Shows Up |
|---|---|
| OpenAI API | Generating questions + judging answers |
| `python-dotenv` | Loading the API key securely from `.env` |
| `for` loop | Running the game for N rounds |
| `f-strings` | Printing score and round info cleanly |
| Score tracking | Incrementing a counter across rounds |
| Prompt engineering | Telling the AI what role to play and what format to use |

---

## 💡 How The AI Does Two Jobs

Unlike the Scooby-Doo project where the AI just picked a move, here the AI does **two separate things**:

1. **Generates** the trivia question based on the topic
2. **Evaluates** the user's answer and replies with correct/incorrect + the right answer

Both happen through `client.responses.create()` — but with different prompts each time.

---

## 🔑 Key Variables

```python
topic = ""          # What the user wants to be quizzed on
rounds = 0          # How many questions to ask
score = 0           # Tracks correct answers
```

---

## 🚀 Built By

**Erdal** — Python student leveling up one project at a time 💪