import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("Key loaded:", bool(api_key))

with open("questions.txt", "r") as file:
    text = file.read()


questions = text.splitlines()

client = genai.Client(api_key=api_key)
responses = []
for question in questions:
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=f"Answer briefly in 2–3 sentences:\n{question}"
    )

    responses.append({
        "question": question,
        "response": response.output_text
    })
    print("Question:", question)
    print("Answer:", response.output_text)
    print()

with open("responses.json", "w", encoding="utf-8") as file:
    json.dump(responses, file, indent=4, ensure_ascii=False)

print("Saved responses to responses.json")
