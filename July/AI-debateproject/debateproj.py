import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Welcome to AI Debate Partner!")

topic = input("Debate topic: ")
side = input("Your side (FOR or AGAINST): ").strip().upper()
rounds = int(input("How many rounds? "))

ai_side = "AGAINST" if side == "FOR" else "FOR"

history = f"Topic: {topic}\nUser side: {side}\nAI side: {ai_side}\n\n"

for i in range(rounds):
    print(f"\n--- Round {i + 1} ---")
    
    user_reply = input("Your argument: ")
    history += f"Round {i + 1} User: {user_reply}\n"

    response = client.responses.create(
        model="gpt-5.5",
        input=f"""
You are an AI debate opponent.
Your side: {ai_side}
User side: {side}

History:
{history}

Respond directly to the user's latest argument. Keep it concise (2-4 sentences).
"""
    )

    ai_reply = response.output_text.strip()
    history += f"Round {i + 1} AI: {ai_reply}\n"
    
    print(f"AI: {ai_reply}")

