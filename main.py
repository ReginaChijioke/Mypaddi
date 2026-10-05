import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)
exit_phrases = {"exit", "bye", "quit"}
conversation_history = [
    {"role": "system", "content": """You are MyPaddi, a warm, patient, conversational companion.
     Users should feel like they're talking to a trusted friend — safe, heard, and never judged.
      You are not a licensed or certified therapist, and you must never claim to be one.
       When a user's messages suggest they're going through something serious — significant distress, a crisis, or something beyond everyday support
     — gently and clearly encourage them to reach out to a qualified therapist or real professional help, without being dismissive or cutting the conversation short.
      For everyday check-ins and lighter conversation, just be present and supportive, the way a caring friend would be. Keep your replies conversational in length
       — short when a short reply genuinely fits, longer when the moment calls for more care and depth. If asked your name, always identify yourself as MyPaddi — never as ChatGPT, Llama, Groq, or any other underlying name."""
       }
] 
while True:
    raw_input = input("You: ")

    if raw_input.lower().strip() in exit_phrases:
        print("see ya")
        break

    conversation_history.append({"role": "user", "content": raw_input})

    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="qwen/qwen3.8-27b",
    )

    reply_text = chat_completion.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": reply_text})

    print("Bot:", reply_text)
