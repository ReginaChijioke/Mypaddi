import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)
exit_phrases = {"exit", "bye", "quit"}
conversation_history = [] 
while True:
    raw_input = input("You: ")

    if raw_input.lower().strip() in exit_phrases:
        print("see ya")
        break

    conversation_history.append({"role": "user", "content": raw_input})

    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="openai/gpt-oss-120b",
    )

    reply_text = chat_completion.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": reply_text})

    print("Bot:", reply_text)
