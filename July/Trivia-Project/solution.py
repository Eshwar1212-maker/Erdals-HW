import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

score = 0

print("Welcome to AI Trivia")

topic = input("Enter a topic: ")
rounds = int(input("How many questions? "))

for i in range(rounds):

    print(f"\n--- Round {i + 1} ---")

    # Generate a question
    response = client.responses.create(
        model="gpt-5.5",
        input=f"""
Create one trivia question about {topic}.

Return it exactly like this:

Question: ...
Answer: ...
"""
    )

    output = response.output_text.strip()

    # Split the AI response into question and answer
    lines = output.split("\n")
    question = lines[0].replace("Question:", "").strip()
    answer = lines[1].replace("Answer:", "").strip()

    print("Question:", question)

    user_answer = input("Your answer: ")

    # Judge the answer
    judge_response = client.responses.create(
        model="gpt-5.5",
        input=f"""
Question: {question}

Correct Answer: {answer}

User Answer: {user_answer}

Reply with only:
CORRECT
or
WRONG
"""
    )